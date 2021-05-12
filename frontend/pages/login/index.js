import Link from "next/link";
import Head from "next/head";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";

import FormTemplate from "../../src/components/Form";
import Header from "../../src/components/Header";

export default function Login() {
  return (
    <>
      <Header />
      <Head>
        <title>Login Page</title>
      </Head>

      <h1>Login Page</h1>
      <Image
        src="/images/profile.png" // Route of the image file
        height={144} // Desired size with correct aspect ratio
        width={144} // Desired size with correct aspect ratio
        roundedCircle
        alt="Guilherme Eisfeld"
      />

      <FormTemplate></FormTemplate>

      <h2>
        <Link href="/">
          <Button>Back to home</Button>
        </Link>
      </h2>
    </>
  );
}
