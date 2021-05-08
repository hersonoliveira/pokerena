import Link from "next/link";
import Image from "next/image";
import Head from "next/head";
import Layout from "../../src/components/Layout";
import Button from "react-bootstrap/Button";

export default function Login() {
  return (
    <Layout>
      <Head>
        <title>Login Page</title>
      </Head>
      <h1>Login Page</h1>
      <Image
        src="/images/profile.jpg" // Route of the image file
        height={144} // Desired size with correct aspect ratio
        width={144} // Desired size with correct aspect ratio
        alt="Guilherme Eisfeld"
      />
      <h2>
        <Link href="/">
          <Button>Back to home</Button>
        </Link>
      </h2>
    </Layout>
  );
}
