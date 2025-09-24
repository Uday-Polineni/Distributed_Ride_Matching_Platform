import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, useMapEvents } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import axios from "axios";

// Fix default marker issue in Leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

function LocationMarker({ setPosition }) {
  useMapEvents({
    click(e) {
      setPosition(e.latlng);
    },
  });
  return null;
}

export default function MapPage() {
  const [riderPos, setRiderPos] = useState(null);
  const [driverPos, setDriverPos] = useState(null);

  const sendRiderRequest = async () => {
    if (!riderPos) return alert("Click on map to select rider location");
    try {
      const res = await axios.post("http://127.0.0.1:5001/rider/request", {
        riderId: "R1",
        lat: riderPos.lat,
        lon: riderPos.lng,
        destination: "Airport", // you can replace with UI input
      });
      alert("Rider Response: " + JSON.stringify(res.data));
    } catch (err) {
      console.error(err);
      alert("Error sending rider request");
    }
  };

  const sendDriverUpdate = async () => {
    if (!driverPos) return alert("Click on map to select driver location");
    try {
      const res = await axios.post("http://127.0.0.1:5002/driver/update", {
        driverId: "D1",
        lat: driverPos.lat,
        lon: driverPos.lng,
        available: true,
      });
      alert("Driver Response: " + JSON.stringify(res.data));
    } catch (err) {
      console.error(err);
      alert("Error sending driver update");
    }
  };

  return (
    <div style={{ height: "100vh" }}>
      <MapContainer
        center={[12.9716, 77.5946]} // Bangalore coords
        zoom={13}
        style={{ height: "90%", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="© OpenStreetMap contributors"
        />
        {riderPos && <Marker position={riderPos}></Marker>}
        {driverPos && <Marker position={driverPos}></Marker>}

        <LocationMarker setPosition={setRiderPos} />
      </MapContainer>

      <div style={{ padding: "10px", textAlign: "center" }}>
        <button onClick={sendRiderRequest}>Send Rider Request</button>
        <button onClick={sendDriverUpdate} style={{ marginLeft: "10px" }}>
          Send Driver Update
        </button>
      </div>
    </div>
  );
}
