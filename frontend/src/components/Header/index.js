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
    >
      <Navbar.Brand href="/">POKERENA</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="menu">
          <Nav.Item>
            <Nav.Link href="/">Home</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/newGame">Novo Jogo</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/ranking">Ranking</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link href="/ranking">Torneios</Nav.Link>
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
