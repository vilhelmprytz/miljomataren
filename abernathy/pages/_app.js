import { SWRConfig } from "swr";
import styles from "../styles/Home.module.css";
import "../styles/globals.css";
import fetch from "../lib/fetchJson";

function App({ Component, pageProps }) {
  return (
    <SWRConfig
      value={{
        fetcher: fetch,
        onError: (err) => {
          console.error(err);
        },
      }}
    >
      <Component {...pageProps} />
      <footer className={styles.footer}>
        <a
          href="https://github.com/vilhelmprytz/miljomataren"
          target="_blank"
          rel="noopener noreferrer"
        >
          github.com/vilhelmprytz/miljomataren
        </a>
      </footer>
    </SWRConfig>
  );
}

export default App;
