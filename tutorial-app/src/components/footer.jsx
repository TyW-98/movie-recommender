import React, { Component } from "react";

class Footer extends Component {
  render() {
    const animals = ["horse", "dog", "cat"];

    return (
      <React.Fragment>
        <h5>This is the footer {this.props.trademark}</h5>
        <p>Passing message from header {this.props.userInput}</p>
        <p>
          {this.props.userInput !== ""
            ? "Footer has been updated"
            : "Enter text into text box and submit"}
        </p>
        <ul>
          {animals.map((animal) => {
            return (
              <React.Fragment key={animal}>
                <li>{animal}</li>
              </React.Fragment>
            );
          })}
        </ul>
      </React.Fragment>
    );
  }
}

export default Footer;
