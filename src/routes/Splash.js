import React from "react";
import Button from "../components/button";
import { useHistory } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import logo from "../assets/logo.svg";
import TextField from "../components/textfield";

const Splash = () => {
  const history = useHistory();
  const nextPage = () => {
    let page = "/home";
    history.push(page);
  };
  return (
    <Container className="splash-container">
      <Row>
        <img className="logo" src={logo} />
        <Col className="text-center" lg={"12"}>
          <h1 style={{ marginBottom: "9.5rem", marginTop: "2rem" }}>
            GITHUB AUTOMATION
          </h1>
        </Col>
        <Col className="input-div" lg={"12"}>
          <TextField
            isRequired={true}
            placeholder="Enter Directory Location"
            name="install"
          />
        </Col>
        <Col className="btn-div" lg={"12"}>
          <Button
            onClick={nextPage}
            text="LISTEN !"
            bgColor="#48BFE3"
            textColor="#343A40"
          />
        </Col>
      </Row>
    </Container>
  );
};

export default Splash;
