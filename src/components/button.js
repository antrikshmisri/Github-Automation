import React from "react";

const Button = (props) => {
  return (
    <button
      style={{ backgroundColor: props.bgColor }}
      className="button btn"
      onClick={props.onClick}
    >
      {props.text}
    </button>
  );
};
export default Button;
