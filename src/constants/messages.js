import TextField from "../components/textfield";
import Button from "../components/button";
import { Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const RepoInputs = () => {
  return (
      <Container>
        <p style={{ margin: "1rem 1rem" }}>Add repo info here</p>
        <Row>
          <Col md={"6"}>
            <TextField isRequired={true} placeholder="URL" name="url"/>
          </Col>
          <Col md={"6"}>
            <TextField isRequired={true} placeholder="Branch" name="branch"/>
          </Col>
        </Row>
      </Container>
  );
};

const messages = {
  foundDirectory: {
    title: "Found the directory",
    text: "Click to get repository info",
    icon: "success",
    confirmButtonText: "Start",
  },
  noRemote: {
    title: "No remote repo info found",
    text: "Add repo info here",
    icon: "error",
    preConfirm: () => {
      return new Promise((resolve) => {
        resolve([
          document.querySelector("input[name = 'url']").value,
          document.querySelector("input[name = 'branch']").value
        ])
      })
    },
    html: (
      <RepoInputs />
    ),
  },
  noDirectory: {
    title: "Oops! No such directory",
    text: "Couldn't find the directory",
    icon: "error",
    confirmButtonText: "Ok",
  },
  foundRemote: {
    title: "Repository info found",
    icon: "success",
    confirmButtonText: "Start",
  },
};

export default messages;
