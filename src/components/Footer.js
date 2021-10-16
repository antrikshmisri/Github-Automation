import React from "react";
import heart from '../assets/heart.svg'

function Footer() {
  return (
    <footer>
      <h1>
        Made with <img src={heart} width={'35px'} /> by <span className="name">Antriksh</span>
      </h1>
    </footer>
  );
}

export default Footer;
