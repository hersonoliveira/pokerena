import { useState, useEffect } from "react";
import { Auth } from "aws-amplify";
import { useRouter } from "next/router";

import Link from "next/link";

import Button from "react-bootstrap/Button";

import Image from "react-bootstrap/Image";


export default function Ranking() {
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
      <h1 className="title">Ranking</h1>
      <p className="description">melhores e piores</p>

      <Image
        src="/images/construction.gif"
        alt="construction"
        className="mainLogo"
      />
      <p className="description">Em construção...</p>
    </>
  );
}
