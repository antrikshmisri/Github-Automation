import { useState, useEffect } from "react";

const useJsonFile = (fileName) => {
  const [jsonData, setJsonData] = useState([]);
  useEffect(() => {
    fetch(fileName)
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
