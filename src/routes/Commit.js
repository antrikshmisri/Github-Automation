import React from "react";
import Button from "../components/button";
import { Container, Row, Carousel, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Header from "../components/Header.js";
import Footer from "../components/Footer.js";
import Card from "../components/card";
import tmp from "../scripts/tmp.json";

const Commit = () => {
  return (
    <>
      <Header />
      <Container>
        <Row>
          <Col lg={"12"}>
            <Carousel indicators={false}>
              {tmp.map((file,idx) => {
                return (
                  <Carousel.Item key={idx}>
                    <Card key={idx} heading={file.path.split('\\').pop()} content={file.changes} />
                  </Carousel.Item>
                );
              })}
            </Carousel>
          </Col>
        </Row>
      </Container>
      <Footer />
    </>
  );
};

export default Commit;
