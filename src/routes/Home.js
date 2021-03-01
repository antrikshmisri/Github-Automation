import React from "react";
import Button from "../components/button";
import { useHistory } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Header from "../components/Header.js";
import Footer from "../components/Footer.js";

const Home = () => {
  const history = useHistory();
  const nextPage = () => {
    let page = "/commit";
    history.push(page);
  };
  return (
    <>
      <Header />
      <div className="text">
        <h1 className="loading mx-0 my-4">Listening</h1>
        <Button
          onClick={nextPage}
          text="VIEW FILES"
          textColor="#CED4DA"
          bgColor="#343A40"
        />
      </div>
      <Footer />
    </>
  );
};

export default Home;
