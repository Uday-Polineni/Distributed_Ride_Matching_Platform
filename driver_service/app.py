from flask import Flask, request, jsonify
from common.kafka_utils import get_producer
from common.redis_utils import get_redis, add_driver_location
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows requests from all origins

producer = get_producer()
r = get_redis()

@app.route("/driver/update", methods=["POST"])
def driver_update():
    data = request.json
    data["timestamp"] = time.time()
    producer.send("driver-updates", data)
    add_driver_location(r, data["driverId"], data["lat"], data["lon"])
    return jsonify({"status": "driver updated", "data": data})

if __name__ == "__main__":
    app.run(port=5002)
