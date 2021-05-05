import { SWRConfig } from "swr";
import "../styles/globals.css";

function App({ Component, pageProps }) {
  return (
    <SWRConfig
      value={{
        fetcher: (...args) => fetch(...args).then((res) => res.json()),
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
