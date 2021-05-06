import Head from "next/head";
import styles from "../styles/Home.module.css";
import useUser from "../lib/useUser";
import useTokens from "../lib/useTokens";

export default function Token({ backendUrl }) {
  const { user } = useUser({ backendUrl: backendUrl, redirectTo: "/login" });
  const { tokens, loadingTokens } = useTokens(backendUrl, user);

  if (!user?.code == 200 || loadingTokens) {
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
          <p>Tokens</p>
          {tokens.response.map((token) => (
            <p>
              #{token.id} - {token.token}
            </p>
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
