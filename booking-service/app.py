from db import cursor, conn
from client import get_queue_number
from producer import send_notification
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

doctors = [
    {
        "id":1,
        "name":"dr. Budi",
        "specialist":"Umum"
    },
    ...
]
queue = []

@app.route('/')
def home():
    return "Doctor Appointment Booking Service Running"


@app.route('/doctors')
def get_doctors():

    cursor.execute(
        "SELECT id, name, specialist FROM doctors"
    )

    doctors = cursor.fetchall()

    result = []

    for doctor in doctors:
        result.append({
            "id": doctor[0],
            "name": doctor[1],
            "specialist": doctor[2]
        })

    return jsonify(result)


@app.route('/booking', methods=['POST'])
def booking():

    try:

        data = request.get_json()

        patient_name = data["patient_name"]
        doctor_id = data["doctor_id"]

        # gRPC
        queue_number = get_queue_number(patient_name)

        # PostgreSQL
        cursor.execute(
            """
            INSERT INTO bookings
            (patient_name, doctor_id, queue_number)
            VALUES (%s,%s,%s)
            """,
            (patient_name, doctor_id, queue_number)
        )

        conn.commit()

        # RabbitMQ
        message = (
            f"Booking successful - "
            f"{patient_name} mendapatkan antrean nomor {queue_number}"
        )

        send_notification(message)

        return jsonify({
            "message": "Booking Successful",
            "queue_number": queue_number
        })

    except Exception as e:

        print("ERROR TERJADI:")
        print(e)

        return jsonify({
            "error": str(e)
        }), 500


@app.route('/queue')
def get_queue():
    return jsonify(queue)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
