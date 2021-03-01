import React from "react";

const Button = (props) => {
  return (
    <button
      style={{ backgroundColor: props.bgColor, color: props.textColor }}
      className="button"
      onClick={props.onClick}
    >
      {props.text}
    </button>
  );
};
export default Button;
