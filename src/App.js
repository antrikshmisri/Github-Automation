import React , {Component , useState} from "react"
import {BrowserRouter as Router , Switch , Route} from "react-router-dom"
import { eel } from "./eel.js";
import Splash from './routes/Splash'
import Home from './routes/Home'
import Header from "./components/Header.js"
import Footer from "./components/Footer.js"
function App() {
  // eel.set_host("ws://localhost:8888");
  return (
    
    <Router>
      <Header />
      <div className="App">
          <Switch>
          <Route path='/' exact component={Splash}/>
          <Route path='/home' component={Home}/>
        </Switch>
       
      </div>
      <Footer />
    </Router>
  );
}
export default App;
