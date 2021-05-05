import useSWR from "swr";
import { useRouter } from "next/router";

export default function Token({ backend_url }) {
  const router = useRouter();
  const { data, error } = useSWR(`${backend_url}/api/token`, fetch);

  if (!data) return <div>loading...</div>;
  if (error || data.status == 401) {
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
        <div>
          <p>Tokens</p>
          {data.response.forEach((token) => {
            return (
              <p>
                #{token.id} - {token.token}
              </p>
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
