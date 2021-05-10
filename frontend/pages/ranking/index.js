import Head from "next/head";
import Link from "next/link";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";

export default function Ranking() {
  return (
    <Container>
      <Head>
        <title>Ranking</title>
      </Head>

      <h2>Ranking</h2>

      <Link href="/">
        <Button>Back to home</Button>
      </Link>
    </Container>
  );
}
