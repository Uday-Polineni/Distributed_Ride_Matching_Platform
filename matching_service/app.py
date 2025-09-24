from flask import Flask, jsonify
from threading import Thread
from common.kafka_utils import get_consumer, get_producer
from common.redis_utils import get_redis, find_nearby_drivers
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows requests from all origins

producer = get_producer()
r = get_redis()

def match_loop():
    consumer = get_consumer("rider-requests", group_id="matcher")
    for msg in consumer:
        rider = msg.value
        lat, lon = rider["lat"], rider["lon"]
        nearby = find_nearby_drivers(r, lat, lon)
        
        if nearby:
            best_driver = nearby[0]  # TODO: improve using ETA heuristics
            match = {
                "riderId": rider["riderId"],
                "driverId": best_driver[0].decode(),
                "distance_km": best_driver[1]
            }
            producer.send("ride-matches", match)
            print("Matched:", match)

@app.route("/health")
def health():
    return jsonify({"status": "matching service running"})

if __name__ == "__main__":
    Thread(target=match_loop, daemon=True).start()
    app.run(port=5003)
