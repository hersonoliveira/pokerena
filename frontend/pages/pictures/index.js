import Head from "next/head";
import Link from "next/link";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";

import Header from "../../src/components/Header";
import Layout from "../../src/components/Layout";

export default function Pictures() {
  return (
    <>

      <h1 className="title">Fotos</h1>
      <p className="description">um show de visual de feiura</p>


      <Link href="/">
        <Button>Back to home</Button>
      </Link>
    </>
  );
}
