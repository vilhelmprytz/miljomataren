import Head from "next/head";
import styles from "../../styles/Home.module.css";
import useUser from "../../lib/useUser";
import useTrip from "../../lib/useTrip";
import usePositions from "../../lib/usePositions";
import dynamic from "next/dynamic";
import { useRouter } from "next/router";

export default function Trip({ backendUrl }) {
  const router = useRouter();
  const { id } = router.query;

  const { user } = useUser({ backendUrl: backendUrl, redirectTo: "/login" });
  const { trip, loadingTrip } = useTrip(backendUrl, user, id);
  const { positions, loadingPositions } = usePositions(backendUrl, user, id);

  if (!user?.code == 200 || loadingTrip || loadingPositions) {
    return <p>loading...</p>;
  }

  const leafletPositions = positions.response.map((position) => {
    return [position.lat, position.lon];
  });

  const Map = dynamic(
    () => import("../../components/Map"),
    { ssr: false, leafletPositions } // This line is important. It's what prevents server-side render
  );

  return (
    <div className={styles.container}>
      <Head>
        <title>Miljömätaren</title>
        <meta name="description" content="Miljömätaren" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Miljömätaren</h1>
        <div>
          <p>Trip #{trip.response.id}</p>
          <br />
          <p>Active: {trip.response.active ? "yes" : "no"}</p>
          <p>Created: {trip.response.trip_started}</p>
          <p>Updated: {trip.response.time_updated}</p>
          {!trip.response.active && <p>Ended: {trip.response.trip_ended}</p>}
          <p>Cost: {trip.response.statistics.trip_cost} kr</p>
          <p>CO2 emissions: {trip.response.statistics.co2_emissions} g</p>
          <p>
            Distance of trip: {trip.response.statistics.distance_travelled} m
          </p>
          <p>Used fuel: {trip.response.statistics.used_fuel} l</p>
        </div>
        <div>
          <Map />
        </div>
      </main>
    </div>
  );
}

export async function getServerSideProps(context) {
  return {
    props: { backendUrl: process.env.BACKEND_URL }, // will be passed to the page component as props
  };
}
