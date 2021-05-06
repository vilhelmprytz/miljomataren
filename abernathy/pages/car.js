import Head from "next/head";
import styles from "../styles/Home.module.css";
import useUser from "../lib/useUser";
import useCars from "../lib/useCars";

export default function Car({ backendUrl }) {
  const { user } = useUser({ backendUrl: backendUrl, redirectTo: "/login" });
  const { cars, loadingCars } = useCars(backendUrl, user);

  if (!user?.code == 200 || loadingCars) {
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
          <p>Cars</p>
          {cars.response.map((car) => (
            <div>
              <p>
                #{car.id} - {car.registration_number}
              </p>
              <p>
                {car.co2_emissions} g/km - {car.fuel_consumption} l/100 km
              </p>
              <br />
            </div>
          ))}
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
