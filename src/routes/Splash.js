import React from 'react'
import Button from '../components/button'
import {useHistory} from 'react-router-dom'
import {Container , Row , Col} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import logo from '../assets/logo.svg'
const Splash = () => {
    const history = useHistory()
    const nextPage = () => {
    let page = '/home'
    history.push(page)
    }
    return (
        <Container className="splash-container">
            <Row>
                <img className="logo" src={logo}></img>
                <Col className="text-center" lg={"12"}>
                    <h1 style={{marginBottom: "9.5rem"}}>GITHUB AUTOMATION</h1>
                </Col>
                <Col className="btn-div" lg={"12"}>
                    <Button onClick={nextPage} text="START" bgColor="#48BFE3"/>
                </Col>
            </Row>
        </Container>
    );
}

export default Splash

