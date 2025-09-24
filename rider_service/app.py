from flask import Flask, request, jsonify
from common.kafka_utils import get_producer
import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows requests from all origins

producer = get_producer()

@app.route("/rider/request", methods=["POST"])
def rider_request():
    data = request.json
    data["timestamp"] = time.time()
    producer.send("rider-requests", data)
    return jsonify({"status": "request sent", "data": data})

if __name__ == "__main__":
    app.run(port=5001)
