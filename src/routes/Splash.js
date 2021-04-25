import React, { useState,useEffect} from "react";
import Button from "../components/button";
import { useHistory } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import logo from "../assets/logo.svg";
import TextField from "../components/textfield";
import swal from "sweetalert2";
import withReactContent from "sweetalert2-react-content";
import { eel } from "../eel";
import messages from "../constants/messages";
import useRepoInfo from "../hooks/useRepoInfo"

const reactSwal = withReactContent(swal);

const Splash = () => {
  const history = useHistory();
  const [dirValue, setDirValue] = useState(
    localStorage.getItem("dirValue") || ""
  );

  useEffect(() => {
    localStorage.setItem("dirValue", dirValue);
  }, [dirValue]);
  
  const [info , setInfo] = useRepoInfo()
  // go to next page
  const nextPage = () => {
    let page = "/home";
    history.push(page);
  };
  // handle input value change
  const handleChange = (event) => {
    setDirValue(event.target.value);
  };
  // handle form submit event
  const handleSubmit = (event) => {
    event.preventDefault();
    // check if entered path is valid
    eel.checkPath(dirValue)((ret) => {
      if (ret) {
        swal.fire(messages.foundDirectory).then((value) => {
          // get remote info from directory

            if (info.includes("n")) {
              // get url , branch from alert inputs

              reactSwal.fire(messages.noRemote).then((value) => {
                let [url, branch] = value.value;
                // run python entrypoint script
                eel.init(url, branch, dirValue)
                nextPage()
              })
              .catch(err => {
                console.log(err)
              });
            } else {
              let [url , branch] = info
              swal.fire({
                ...messages.foundRemote,
                html: `<a onclick="window.open('${url}', '${url}')" href="javascript:void()">${url}</a> <br/> <p>${branch}</p>`,
              }).then(value => {
                eel.init(url, branch, dirValue)
                nextPage()
              })
            }

        });
      } 
      // if path not valid show noDir alert
      else {
        swal.fire(messages.noDirectory);
      }
    });
  };
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
              onChange={handleChange}
              value={dirValue}
            />
          </Col>
          <Col className="btn-div" lg={"12"}>
            <Button
              onClick={handleSubmit}
              text="LISTEN !"
              bgColor="#495057"
              textColor="#dee2e6"
            />
          </Col>
        </form>
      </Row>
    </Container>
  );
};

export default Splash;
