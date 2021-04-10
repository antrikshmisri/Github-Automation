import { useState, useEffect } from "react";
import header from "../constants/headers"
const useJsonFile = (fileName) => {
  const [jsonData, setJsonData] = useState([]);
  useEffect(() => {
    fetch(fileName , header)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setJsonData(data);
      });
  }, []);

  return [jsonData , setJsonData]
};

export default useJsonFile
