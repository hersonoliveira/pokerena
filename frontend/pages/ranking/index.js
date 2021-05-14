import Link from "next/link";

import Button from "react-bootstrap/Button";

export default function Ranking() {
  return (
    <>
      <h1 className="title">Ranking</h1>
      <p className="description">melhores e piores</p>

      <Link href="/">
        <Button>Back to home</Button>
      </Link>
    </>
  );
}
