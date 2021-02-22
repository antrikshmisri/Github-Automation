import "./App.css";
import React , {Component , useState} from "react"
import { eel } from "./eel.js";


function App() {
  let [value , setValue] = useState('')
  eel.set_host("ws://localhost:8888");
  eel.getpara("argument")(res => setValue(value = res))
  return (
    <div className="App">
        <div className="Main">
          <h1>Hello</h1>
          <p>{value}</p>
        </div>
    </div>
  );
}
export default App;
