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
            <Nav.Link href="/">Home</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/newGame">Novo Jogo</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/ranking">Ranking</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/tournament">Torneios</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/pictures">Imagens</Nav.Link>
          </Nav.Item>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default Header;
