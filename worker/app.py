from flask import Flask
import os
import time
import random

app = Flask(__name__)

WORKER = os.environ["WORKER_NAME"]


@app.route('/bookAppointment')
def book_appointment():

    duration = random.randint(3, 5)

    time.sleep(duration)

    msg = f"{WORKER} finished booking ({duration}s)"

    print(msg, flush=True)

    return msg


@app.route('/getDoctors')
def get_doctors():

    duration = random.randint(3, 5)

    time.sleep(duration)

    msg = f"{WORKER} finished doctor service ({duration}s)"

    print(msg, flush=True)

    return msg


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7000,
        threaded=True
    )