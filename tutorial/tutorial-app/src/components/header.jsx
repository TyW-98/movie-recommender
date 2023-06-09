import React, { useState } from "react";

function Header(props) {
  const [inputValue, setInputValue] = useState("");

  const handleInputValue = (event) => {
    setInputValue(event.target.value);
  };

  const handleButtonClick = () => {
    props.userInput(inputValue);
  };

  return (
    <React.Fragment>
      <h1>welcome {props.username}</h1>
      <h5>your number is {props.id}</h5>
      <input type="text" value={inputValue} onChange={handleInputValue} />
      <button onClick={handleButtonClick}>Update</button>
    </React.Fragment>
  );
}

export default Header;
