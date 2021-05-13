import Head from "next/head";
import Link from "next/link";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";

import Header from "../../src/components/Header";
import Layout from "../../src/components/Layout";

export default function NewGame() {
  return (
    <Layout>
      <h2>Começando um novo Torneio</h2>

      <Link href="/">
        <Button>Back to home</Button>
      </Link>
    </Layout>
  );
}
