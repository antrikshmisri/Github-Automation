import React from "react";
import { Container, Row, Carousel, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Header from "../components/Header.js";
import Footer from "../components/Footer.js";
import Card from "../components/card";
import useJsonFile from "../hooks/useJsonFile";
import useArray from "../hooks/useArray";
import { eel } from "../eel.js";
import { useState } from "react";
import FadeLoader from "react-spinners/FadeLoader";
import spinnerStyle from "../constants/spinnerStyle";
// import tmp from "../scripts/tmp.json";

const Commit = () => {
  const [jsonData,] = useJsonFile("./tmp.json");
  const [message, setMessage] = useArray(jsonData.length);
  const [info,] = useState([]);
  const [isLoading, setLoading] = useState(false);
  const dirValue = localStorage.getItem("dirValue");

  const handleSubmit = (file, diff, message, idx, event) => {
    event.preventDefault();
    setLoading(true);
    if (event.target.name === "discard") {
      setMessage("-r", idx);
    }
    const [url, branch] = info;
    eel.commitAndUpdate(
      dirValue,
      file,
      idx,
      message[idx],
      url,
      branch
    )((ret) => {
      setLoading(false);
      ret ? console.log("Pushed!") : console.log("Reverted");
    });
  };

  const handleChange = (event, idx) => {
    setMessage(event.target.value, idx);
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
                        fullPath={file.path}
                        content={file.changes}
                        loading={isLoading}
                        onChange={(e) => {
                          handleChange(e, idx);
                        }}
                        onSubmit={(e) => {
                          handleSubmit(
                            file.path,
                            file.changes,
                            message,
                            idx,
                            e
                          );
                        }}
                        value={message[idx]}
                      >
                        <FadeLoader
                          color={"#fff"}
                          loading={isLoading}
                          className="spinner"
                          css={spinnerStyle}
                        />
                      </Card>
                    </Carousel.Item>
                  );
                })}
              </Carousel>
            ) : (
              <h1 style={{ opacity: "0.5", textAlign: "center" }}>
                All set! No changes to push
              </h1>
            )}
          </Col>
        </Row>
      </Container>
      <Footer />
    </>
  );
};

export default Commit;
