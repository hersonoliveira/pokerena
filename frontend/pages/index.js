import Head from "next/head";
import Link from "next/link";


import Image from "react-bootstrap/Image";

export default function Home() {
  return (
    <div className="container">
      <Head>
        <title>POKERENA</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className="title">POKERENA</h1>
        {/* <Link href="/login">
          <Button>Login by clicking here!</Button>
        </Link> */}

        <p className="description">A Jogatina da Quarentena</p>

        <Image src="/images/sexy.png" alt="sexy poker" className="mainLogo" />

        <div className="grid">
          <a href="/newGame" className="card">
            <h3>Começar Novo Torneio &rarr;</h3>
            <p>Comece a jogatina.</p>
          </a>

          <a href="/ranking" className="card">
            <h3>Ranking &rarr;</h3>
            <p>Veja quem manda na porra toda!</p>
          </a>

          <a
            href="/tournament"
            className="card"
          >
            <h3>Torneios &rarr;</h3>
            <p>Confira jogo a jogo, lance a lance.</p>
          </a>

          <a
            href="/pictures"
            className="card"
          >
            <h3>Fotos &rarr;</h3>
            <p>
              Retratos alcoolizados da balbúrdia
            </p>
          </a>
        </div>
      </main>

      <footer>
        <a
          href="https://github.com/campodegelo"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{" "}
          <img src="/images/campodegelo.png" alt="Vercel Logo" className="logo" />
        </a>
      </footer>
    </div>
  );
}
