import { MapContainer, TileLayer, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const Map = ({ leafletPositions }) => {
  return (
    <MapContainer
      center={[59.324416, 18.046431]}
      zoom={13}
      scrollWheelZoom={true}
      style={{ height: 400, width: "100%" }}
    >
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Polyline
        pathOptions={{ color: "purple" }}
        positions={leafletPositions}
      />
    </MapContainer>
  );
};

export default Map;
