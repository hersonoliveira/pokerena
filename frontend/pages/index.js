import Link from "next/link";

import Button from "react-bootstrap/Button";
import Image from "react-bootstrap/Image";

import FormTemplate from "../src/components/Form";
import Layout from "../src/components/Layout";

import { useState, useEffect } from "react";
import { Auth } from "aws-amplify";
import { useRouter } from "next/router";

export default function Home() {
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
      <h1 className="title">Seja bem vindo</h1>
      <p className="description">{user.username}</p>

      <Image
        src="/images/fizo.jfif"
        alt="fizo"
        roundedCircle
        className="mainLogo"
      />

      <div className="grid">
        <a href="/newGame" className="card">
          <h3>Começar Novo Torneio &rarr;</h3>
          <p>Comece a jogatina.</p>
        </a>

        <a href="/ranking" className="card">
          <h3>Ranking &rarr;</h3>
          <p>Veja quem manda na porra toda!</p>
        </a>

        <a href="/tournament" className="card">
          <h3>Torneios &rarr;</h3>
          <p>Confira jogo a jogo, lance a lance.</p>
        </a>

        <a href="/pictures" className="card">
          <h3>Fotos &rarr;</h3>
          <p>Retratos alcoolizados da balbúrdia</p>
        </a>
      </div>
    </>
  );
}
