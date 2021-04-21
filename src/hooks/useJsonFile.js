import { useState, useEffect } from "react";
import header from "../constants/headers"
const useJsonFile = (fileName) => {
  const [jsonData, setJsonData] = useState([]);
  useEffect(() => {
    fetch(`${process.env.PUBLIC_URL}/${fileName}` , header)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setJsonData(data);
        console.log(jsonData)
      });
  }, []);

  return [jsonData , setJsonData]
};

export default useJsonFile
