import Link from "next/link";
import { css } from "@emotion/css";
import Amplify from "aws-amplify";
import config from "../src/aws-exports";
Amplify.configure({
  ...config,
  ssr: true,
});

import "bootstrap/dist/css/bootstrap.min.css";
import "../src/css/style.css";

import Layout from "../src/components/Layout";

import Head from "next/head";

const linkStyle = css`
  margin-right: 20px;
  cursor: pointer;
`;
const navStyle = css`
  display: flex;
`;

export default function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Head>
        <title>POKERENA</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

        <Component {...pageProps} />
    </Layout>
  );
}
