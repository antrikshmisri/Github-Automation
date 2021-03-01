import React, { useState } from "react";
import Button from "../components/button";
import { useHistory } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import logo from "../assets/logo.svg";
import TextField from "../components/textfield";
import swal from 'sweetalert';
import {eel} from '../eel'


const Splash = () => {
  const history = useHistory();
  const [dirValue , setDirValue] = useState("")
  const nextPage = () => {
    let page = "/home";
    history.push(page);
  };
  const handleChange = (event) => {
    setDirValue(event.target.value)
  }
  const handleSubmit = (event) => {
    event.preventDefault()
    eel.checkPath(dirValue)(ret => {
      if(ret)
      {
        swal({
          title: "Found the directory",
          text: "Click to start the script",
          icon: "success",
          button: "Start",
        })
        .then(
          nextPage
        )
      }
      else
      {
        swal({
          title: "Oops! No such directory",
          text: "Couldn't find the directory",
          icon: "error",
          button: "Ok",
        })
      }
    })
  }
  return (
    <Container className="splash-container">
      <Row>
        <img className="logo" src={logo} />
        <Col className="text-center" lg={"12"}>
          <h1 style={{ marginBottom: "9.5rem", marginTop: "2rem" }}>
            GITHUB AUTOMATION
          </h1>
        </Col>
        <form>
          <Col className="input-div" lg={"12"}>
            <TextField
              isRequired={true}
              placeholder="Enter Directory Location"
              name="install"
              onChange = {handleChange}
              value = {dirValue}
            />
          </Col>
          <Col className="btn-div" lg={"12"}>
            <Button
              onClick={handleSubmit}
              text="LISTEN !"
              bgColor="#48BFE3"
              textColor="#343A40"
            />
          </Col>
        </form>
      </Row>
    </Container>
  );
};

export default Splash;
