import React from "react";
import Button from "../components/button";
import TextField from "../components/textfield";
import { Col, Container, Row } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const Card = (props) => {
  return (
    <Col className="text-center file-card" md={"6"}>
      <Container className="file-content">
        <h1>
          <span>
            <img src={props.image} />
          </span>
          {props.heading}
        </h1>
        <p className="lead">{props.content}</p>
        <hr />
      </Container>
      <Container className="file-btn">
        <Row>
          <Col md={"12"}>
            <TextField placeholder="Commit Msg" name="commit" />
          </Col>
          <Col className="commit-btn" md={"6"}>
            <Button bgColor="#48BFE3" textColor="#343A40" text="Commit" />
          </Col>
          <Col className="reject-btn" md={"6"}>
            <Button bgColor="#E81224" textColor="#343A40" text="Discard" />
          </Col>
        </Row>
      </Container>
    </Col>
  );
};

export default Card;
