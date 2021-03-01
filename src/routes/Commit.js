import React from "react"
import Button from "../components/button";
import { Container, Row , Carousel , Col} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import Header from "../components/Header.js";
import Footer from "../components/Footer.js";
import Card from '../components/card'

const Commit = () => {
    return (
        <>
        <Header />
        <Container>
            <Row>
                <Col lg={"12"}>
                <Carousel indicators={false}>
                    <Carousel.Item>
                        <Card heading="Test-Card" content="Test content paragraph" />
                    </Carousel.Item>
                    <Carousel.Item>
                        <Card heading="Test-Card" content="Test content paragraph" />
                    </Carousel.Item>
                </Carousel>
                </Col>
            </Row>
        </Container>
        <Footer />
        </>
    );
}

export default Commit