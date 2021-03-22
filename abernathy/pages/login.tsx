import Head from "next/head";
import Layout, { siteTitle } from "../components/layout";
import utilStyles from "../styles/utils.module.css";
import useSWR from "swr";
import Link from "next/link";

export default function Login() {
  const data = null;
  // const { data } = useSWR<{
  //   login_url: string;
  // }>("/api/auth/login", fetch);

  // if (!data) return <div>loading...</div>;

  return (
    <Layout>
      <Head>
        <title>{siteTitle} - Login</title>
      </Head>
      <section className={utilStyles.headingMd}>
        {data ? (
          <p>Login</p>
        ) : (
          //   <Link href={data.login_url}>
          //     <a>Login</a>
          //   </Link>
          <p>loading...</p>
        )}
      </section>
    </Layout>
  );
}
