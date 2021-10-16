import React from "react";

const TextField = (props) => {
  return (
    <input
      required={props.isRequired}
      placeholder={props.placeholder}
      name={props.name}
      onChange={props.onChange}
      value={props.value}
    >
      {props.children}
    </input>
  );
};

export default TextField;
