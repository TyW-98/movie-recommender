import React from "react";

function Header(props) {
  return (
    <React.Fragment>
      <h1>welcome {props.username}</h1>
      <h5>your number is {props.id}</h5>
    </React.Fragment>
  );
}

export default Header;
