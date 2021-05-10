import Head from "next/head";
import Link from "next/link";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";

export default function NewGame() {
  return (
    <Container>
      <Head>
        <title>Começando um novo Torneio</title>
      </Head>

      <h2>Começando um novo Torneio</h2>

      <Link href="/">
        <Button>Back to home</Button>
      </Link>
    </Container>
  );
}
