import {AmplifySignOut } from "@aws-amplify/ui-react";

import { useState, useEffect } from "react";
import { Auth } from "aws-amplify";

import Link from "next/link";

import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

const Header = (props) => {
  const [logout, setLogout] = useState(false);

  useEffect(() => {
    // Acessa a sessão do usuário no cliente
    Auth.currentAuthenticatedUser()
      .then((user) => {
        console.log("User: ", user);
        setLogout(true);
      })
      .catch((err) => setLogout(false));
  }, []);



  return (
    <Navbar
      className="header"
      collapseOnSelect
      bg="dark"
      variant="dark"
      expand="sm"
      fixed
    >
      <Link href="/" passHref>
        <Navbar.Brand>POKERENA</Navbar.Brand>
      </Link>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="container-fluid">
          <Nav.Item className="ml-auto">
            <Link href="/" passHref>
              <Nav.Link>Home</Nav.Link>
            </Link>
          </Nav.Item>
          <Nav.Item>
            <Link href="/newGame" passHref>
              <Nav.Link>Novo Jogo</Nav.Link>
            </Link>
          </Nav.Item>
          <Nav.Item>
            <Link href="/ranking" passHref>
              <Nav.Link>Ranking</Nav.Link>
            </Link>
          </Nav.Item>
          <Nav.Item>
            <Link href="/tournament" passHref>
              <Nav.Link>Torneios</Nav.Link>
            </Link>
          </Nav.Item>
          <Nav.Item>
            <Link href="/pictures" passHref>
              <Nav.Link>Imagens</Nav.Link>
            </Link>
          </Nav.Item>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Header;
