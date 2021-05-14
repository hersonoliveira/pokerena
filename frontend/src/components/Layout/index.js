import Footer from "../Footer";
import Header from "../Header";

const layoutStyle = {
  display: "flex",
  flexDirection: "column",
  height: "100%",
  width: "100%",
  minHeight: "100vh",
};

const contentStyle = {
  flex: 1,
  display: "flex",
  flexDirection: "column",
  minHeight: "75vh",
  alignItems: "center",
};

const Layout = (props) => {
  return (
    <div className="Layout" style={layoutStyle}>
      <Header />
      <main>
        <div className="Content">{props.children}</div>
      </main>
      <Footer />
    </div>
  );
};

export default Layout;
