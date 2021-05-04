import Head from "next/head";
import styles from "../../styles/Home.module.css";
import useSWR from "swr";
import { useRouter } from "next/router";
import fetcher from "../../src/fetcher";

export default function Trip({ backend_url }) {
  const router = useRouter();
  const { id } = router.query;
  const { data, error } = useSWR(`${backend_url}/api/trip/${id}`, fetcher);

  if (!data) return <div>loading...</div>;

  if (error || data.code == 401) {
    Router.push("/login");
    return <p>Redirecting..</p>;
  }

  if (data.code == 200) {
    return (
      <div className={styles.container}>
        <Head>
          <title>Miljömätaren</title>
          <meta name="description" content="Miljömätaren" />
        </Head>

        <main className={styles.main}>
          <h1 className={styles.title}>Miljömätaren</h1>
          <p>Logged in as {data.response}</p>
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
  } else {
    return <p>loading..</p>;
  }
}

export async function getServerSideProps(context) {
  return {
    props: { backend_url: process.env.BACKEND_URL }, // will be passed to the page component as props
  };
}
