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
    </SWRConfig>
  );
}

export default App;
