import Footer from "../Footer";
import Header from "../Header";

const layoutStyle = {
  display: "flex",
  flexDirection: "column",
  height: "100%",
  width: "100%",
};

const contentStyle = {
  flex: 1,
  display: "flex",
  flexDirection: "column",
  minHeight: "75vh",
};

const Layout = (props) => {
  return (
    <div className="Layout" style={layoutStyle}>
      <Header />
      <div className="Content" style={contentStyle}>
        {props.children}
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
