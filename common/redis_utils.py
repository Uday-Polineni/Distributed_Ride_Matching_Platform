import redis

def get_redis():
    return redis.Redis(host="a.b.c.d", port=6379, db=0) # your IP here

def add_driver_location(r, driver_id, lat, lon):
    r.geoadd("drivers:location", (lon, lat, driver_id))

def find_nearby_drivers(r, lat, lon, radius_km=5):
    return r.georadius("drivers:location", lon, lat, radius_km, unit="km", withdist=True)
