import React, { Component } from "react";
import { Context } from "../main";
import styled from "styled-components";

const BulletPoint = styled.ul`
  list-style-type: none;
`;

class Footer extends Component {
  render() {
    return (
      <React.Fragment>
        <h5>This is the footer {this.props.trademark}</h5>
        <p>Passing message from header {this.props.userInput}</p>
        <p>
          {this.props.userInput !== ""
            ? "Footer has been updated"
            : "Enter text into text box and submit"}
        </p>
        <Context.Consumer>
          {({ animals }) => (
            <BulletPoint>
              {animals.map((animal) => {
                return (
                  <React.Fragment key={animal}>
                    <li>{animal}</li>
                  </React.Fragment>
                );
              })}
            </BulletPoint>
          )}
        </Context.Consumer>
      </React.Fragment>
    );
  }
}

export default Footer;
