import Head from "next/head";
import Link from "next/link";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";

import Header from "../../src/components/Header";

export default function Pictures() {
  return (
    <>
      <Header />
      <Head>
        <title>Fotos</title>
      </Head>

      <h2>Fotos</h2>

      <Link href="/">
        <Button>Back to home</Button>
      </Link>
    </>
  );
}
