import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { eel } from "./eel.js";
import Splash from "./routes/Splash";
import Home from "./routes/Home";
import Commit from "./routes/Commit";
function App() {
  eel.set_host("ws://localhost:8888");
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={Splash} />
          <Route path="/home" component={Home} />
          <Route path="/commit" component={Commit} />
        </Switch>
      </div>
    </Router>
  );
}
export default App;
