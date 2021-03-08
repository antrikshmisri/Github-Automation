import React from "react";
import { Container, Row, Carousel, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Header from "../components/Header.js";
import Footer from "../components/Footer.js";
import Card from "../components/card";
import useJsonFile from "../hooks/useJsonFile";
import { eel } from "../eel.js";
import { useEffect, useState } from "react";
// import tmp from "../scripts/tmp.json";

const Commit = () => {
  const [jsonData, setJsonData] = useJsonFile("./tmp.json");
  const [message, setMessage] = useState("");
  const [info, setInfo] = useState([]);
  const dirValue = localStorage.getItem("dirValue");

  useEffect(() => {
    setInfo(localStorage.getItem("repoInfo").split(","));
  }, []);

  const handleSubmit = (file, message, event) => {
    event.preventDefault();
    console.log(info, jsonData, message);
    if (event.target.name === "discard") {
      setMessage("-r");
    }
    const [url, branch] = info;
    eel.commitAndUpdate(
      dirValue,
      file,
      message,
      url,
      branch
    )((ret) => {
      console.log(ret)
      ret ? console.log("Pushed!") : console.log("Reverted");
    });
  };

  const handleChange = (event) => {
    setMessage(event.target.value);
  };
  return (
    <>
      <Header />
      <Container>
        <Row>
          <Col lg={"12"}>
            {jsonData.length ? (
              <Carousel indicators={false}>
                {jsonData.map((file, idx) => {
                  return (
                    <Carousel.Item key={idx}>
                      <Card
                        key={idx}
                        heading={file.path.split("\\").pop()}
                        content={file.changes}
                        onChange={handleChange}
                        onSubmit={(e) => {
                          handleSubmit(file.path, message, e);
                        }}
                        value={message}
                      />
                    </Carousel.Item>
                  );
                })}
              </Carousel>
            ) : (
              <h1 style={{ opacity: "0.5" }}>All set! No changes to push</h1>
            )}
          </Col>
        </Row>
      </Container>
      <Footer />
    </>
  );
};

export default Commit;
