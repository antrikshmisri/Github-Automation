import React from "react";
import Button from "../components/button";
import TextField from "../components/textfield";
import { Col, Container, Row } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const Card = (props) => {
  return (
    <Col className=" file-card" md={"6"}>
      <div className="file-content">
        <h1>
          <span>
            <img src={props.image} />
          </span>
          {props.heading}
        </h1>
        <div className="code-block">
          <code>{props.content}</code>
        </div>
        <hr />
      </div>

      <Container className="file-btn">
        <Row>
          <form onSubmit={props.onSubmit}>
            <Col className="input-div" lg={"12"}>
              <TextField
                isRequired={true}
                placeholder="Commit Msg"
                name="commit"
                onChange={props.onChange}
                value={props.value}
              />
            </Col>
            <Col className="commit-btn" lg={"6"}>
              <Button
                name="commit"
                bgColor="#48BFE3"
                textColor="#343A40"
                text="Commit"
              />
            </Col>
            <Col className="reject-btn" lg={"6"}>
              <Button
                name="discard"
                bgColor="#E81224"
                textColor="#343A40"
                text="Discard"
              />
            </Col>
          </form>
        </Row>
      </Container>
    </Col>
  );
};

export default Card;
