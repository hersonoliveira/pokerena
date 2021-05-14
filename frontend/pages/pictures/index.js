import { useState, useEffect } from "react";
import { Auth } from "aws-amplify";
import { useRouter } from "next/router";

import Head from "next/head";
import Link from "next/link";

import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";

import Header from "../../src/components/Header";
import Layout from "../../src/components/Layout";

import Image from "react-bootstrap/Image";


export default function Pictures() {
  const [user, setUser] = useState(null);
  const router = useRouter();

  useEffect(() => {
    Auth.currentAuthenticatedUser()
      .then((user) => setUser(user))
      // Se o usuário não estiver autenticado, redirecione ele para a página `/profile`
      .catch(() => router.push("/login"));
  }, []);
  if (!user) return null;
  return (
    <>
      <h1 className="title">Fotos</h1>
      <p className="description">um show de visual de feiura</p>

      <Image
        src="/images/construction.gif"
        alt="construction"
        className="mainLogo"
      />
      <p className="description">Em construção...</p>
    </>
  );
}
