import React, { useState } from "react";
import "./App.css";

import Header from "./components/header.jsx";
import Footer from "./components/footer.jsx";

function App() {
  const [userInput, setUserInput] = useState("");

  const handleUserInput = (input) => {
    setUserInput(input);
  };

  return (
    <>
      <div className="App">
        <Header username="User1" id="1" userInput={handleUserInput} />
        <Footer trademark="TyW-98" userInput={userInput} />
      </div>
    </>
  );
}

export default App;
