from flask import Flask
import requests

app = Flask(__name__)

workers = [
    "http://worker1:7000",
    "http://worker2:7000",
    "http://worker3:7000"
]

current = 0


@app.route('/<path:path>')
def balance(path):

    global current

    target = workers[current]

    current = (current + 1) % len(workers)

    response = requests.get(
        f"{target}/{path}"
    )

    return response.text


app.run(
    host="0.0.0.0",
    port=7000,
    threaded=True
)