import React from "react";
import Button from "../components/button";
import TextField from "../components/textfield";
import { Col, Container, Row } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import DiffViewer from "./diffViewer";
import { eel } from "../eel";

const Card = (props) => {
  const dirValue = localStorage.getItem("dirValue");
  const [diff, setDiff] = React.useState(null);
  const [showDiffContainer, setShowDiffContainer] = React.useState(false);

  eel.getDiff(
    dirValue,
    props.fullPath
  )((diff) => {
    setDiff(diff);
  });
  return (
    <>
      <Col className=" file-card" md={"6"}>
        {props.children}
        {props.loading ? <div className="dim-overlay" /> : <></>}
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
          <form>
            <Row>
              <Col className="input-div" lg={"12"}>
                <TextField
                  isRequired={true}
                  placeholder="Commit Msg"
                  name="commit-field"
                  onChange={props.onChange}
                  value={props.value}
                />
              </Col>
              <Col className="commit-btn" md={"6"}>
                <Button
                  onClick={props.onSubmit}
                  name="commit"
                  bgColor="#48BFE3"
                  textColor="#343A40"
                  text="Commit"
                />
              </Col>
              <Col className="reject-btn" md={"6"}>
                <Button
                  onClick={props.onSubmit}
                  name="discard"
                  bgColor="#495057"
                  textColor="#dee2e6"
                  text="Discard"
                />
              </Col>
            </Row>
          </form>
          <Row>
            <Col md={6}></Col>
            <Col className="diff-btn" md={6}>
              <a
                onClick={() => {
                  setShowDiffContainer(true);
                }}
                color="#343A40"
                className="diff-btn"
              >
                Raw Diff
              </a>
            </Col>
          </Row>
        </Container>
        {showDiffContainer ? (
          <DiffViewer diff={diff} setShowDiffContainer={setShowDiffContainer} />
        ) : (
          <></>
        )}
      </Col>
    </>
  );
};

export default Card;
