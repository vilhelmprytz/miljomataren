import Head from "next/head";
import styles from "../styles/Home.module.css";
import useSWR from "swr";
import Link from "next/link";
import { useRouter } from "next/router";

export default function Dashboard({ backend_url }) {
  const router = useRouter();
  const { data: user, error: userError } = useSWR(`${backend_url}/api/user`);
  const { data: trips, error: tripsError } = useSWR(`${backend_url}/api/trip`);

  if (!user || !trips) return <div>loading...</div>;

  if (userError || user.status == 401) {
    router.push("/login");
    return <p>Redirecting..</p>;
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Miljömätaren</title>
        <meta name="description" content="Miljömätaren" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Miljömätaren</h1>
        <p>Logged in as {user.response.name}</p>

        <div>
          <p>Trips</p>
          {trips.response.forEach((trip) => {
            return (
              <Link href={`/trip/${trip.id}`}>
                <p>#{trip.id}</p>
              </Link>
            );
          })}
        </div>
      </main>
    </div>
  );
}

export async function getServerSideProps(context) {
  return {
    props: { backend_url: process.env.BACKEND_URL }, // will be passed to the page component as props
  };
}
