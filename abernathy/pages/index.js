import useSWR from "swr";
import Router from "next/router";

export default function Home({ backend_url }) {
  const { data, error } = useSWR(`${backend_url}/api/user`, fetch);

  if (!data) return <div>loading...</div>;
  if (error || data.status == 401) {
    Router.push("/login");
    return <p>Redirecting..</p>;
  }

  if (data.status == 200) {
    Router.push("/dashboard");
    return <p>Redirecting..</p>;
  }
}

export async function getServerSideProps(context) {
  return {
    props: { backend_url: process.env.BACKEND_URL }, // will be passed to the page component as props
  };
}
