import Head from "next/head";
import Link from "next/link";

import Image from "react-bootstrap/Image";

import Layout from "../src/components/Layout";

export default function Home() {
  return (
    <Layout>
      <h1 className="title">POKERENA</h1>
      <p className="description">A Jogatina da Quarentena</p>

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
    </Layout>
  );
}
