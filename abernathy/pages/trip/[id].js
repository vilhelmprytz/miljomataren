import Head from "next/head";
import styles from "../../styles/Home.module.css";
import useUser from "../../lib/useUser";
import useTrip from "../../lib/useTrip";
import { useRouter } from "next/router";

export default function Trip({ backendUrl }) {
  const router = useRouter();
  const { id } = router.query;

  const { user } = useUser({ backendUrl: backendUrl, redirectTo: "/login" });
  const { trip, loadingTrip } = useTrip(backendUrl, user, id);

  if (!user?.code == 200 || loadingTrip) {
    return <p>loading...</p>;
  }

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
          <p>Active: {trip.response.active}</p>
          <p>Cost: {trip.response.statistics.trip_cost} kr</p>
          <p>CO2 emissions: {trip.response.statistics.co2_emissions} g</p>
          <p>
            Distance of trip: {trip.response.statistics.distance_travelled} m
          </p>
          <p>Used fuel: {trip.response.statistics.used_fuel} l</p>
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://github.com/vilhelmprytz/miljomataren"
          target="_blank"
          rel="noopener noreferrer"
        >
          github.com/vilhelmprytz/miljomataren
        </a>
      </footer>
    </div>
  );
}

export async function getServerSideProps(context) {
  return {
    props: { backendUrl: process.env.BACKEND_URL }, // will be passed to the page component as props
  };
}