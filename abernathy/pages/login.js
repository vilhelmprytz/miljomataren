import Head from "next/head";
import styles from "../styles/Home.module.css";

export default function Login({ login_uri, success }) {
  return (
    <div className={styles.container}>
      <Head>
        <title>Miljömätaren - Login</title>
        <meta name="description" content="Miljömätaren" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Miljömätaren</h1>
        {success && (
          <a href={login_uri} rel="noopener noreferrer">
            Login
          </a>
        )}
        {!success && <p>API connection failed - login unavailable.</p>}
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
  const res = await fetch(`${process.env.BACKEND_URL}/api/auth/login`);
  const data = await res.json();

  if (!data.response.login_uri) {
    return {
      props: { success: false },
    };
  }

  return {
    props: { login_uri: data.response.login_uri, success: true }, // will be passed to the page component as props
  };
}
