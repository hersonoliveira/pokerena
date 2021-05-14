import Link from "next/link";

import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

const Header = (props) => {
  return (
    <Navbar
      className="header"
      collapseOnSelect
      bg="dark"
      variant="dark"
      expand="sm"
      fixed
    >
      <Navbar.Brand href="/">POKERENA</Navbar.Brand>
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
