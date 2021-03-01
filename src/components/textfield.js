import React from "react";

const TextField = (props) => {
  return (
    <input
      required={props.isRequired}
      placeholder={props.placeholder}
      name={props.name}
    >
      {props.children}
    </input>
  );
};

export default TextField;
