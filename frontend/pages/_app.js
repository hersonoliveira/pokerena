import "bootstrap/dist/css/bootstrap.min.css";
import "../src/css/style.css";

import Head from "next/head";

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>POKERENA</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Component {...pageProps} />
    </>
  );
}
