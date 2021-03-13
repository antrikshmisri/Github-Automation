import React from "react";
import { useState } from "react";

const useArray = (length) => {
  const [array, _setArray] = useState(new Array(length).join(".").split("."));

  const setArray = (value, idx) => {
    array.splice(idx, 1, value);
    _setArray([...array]);
  };

  return [array, setArray];
};

export default useArray;
