import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import CountryOptions from "./CountryOptions";
import DOBOptions from "./DOBOptions";

export default function RegisterForm(props) {
  const [dateOfBirth, setDateOfBirth] = useState({
    day: "",
    month: "",
    year: "",
  });

  const formElements = [
    { label: "Email", name: "email", id: "email" },
    { label: "Username", name: "username", id: "register-username" },
    { label: "Password", name: "password", id: "register-password" },
    { label: "Confirmation Password", name: "password2", id: "password2" },
    { label: "Preferred Name", name: "preferred_name", id: "preferred-name" },
    { label: "Date of Birth", name: "dob", id: "dob" },
    { label: "Gender", name: "gender", id: "gender" },
    { label: "Country", name: "country", id: "country" },
  ];

  function setDate(event) {
    const { name, value } = event.target;
    setDateOfBirth((prevDateOfBirth) => {
      return {
        ...prevDateOfBirth,
        [name]: value,
      };
    });
  }

  return (
    <div className="modal">
      <div className="register-container">
        <FontAwesomeIcon
          icon={faXmark}
          onClick={props.handleOpenRegisterModal}
          className="close-modal-btn"
        />
        <h2>Create a new account</h2>
        <form className="register-form">
          {formElements.map((element) => {
            return (
              <div key={element.id}>
                <label htmlFor={element.id}>
                  <strong>{element.label}</strong>
                </label>
                {element.id === "country" ? (
                  <CountryOptions />
                ) : element.id === "dob" ? (
                  <DOBOptions dateOfBirth={dateOfBirth} />
                ) : (
                  <input
                    type={
                      element.name === "email"
                        ? "email"
                        : element.name === "password" ||
                          element.name === "password2"
                        ? "password"
                        : "text"
                    }
                    name={element.name}
                    id={element.id}
                  />
                )}
              </div>
            );
          })}
          <button type="submit" className="register-btn">
            Join Now
          </button>
        </form>
      </div>
    </div>
  );
}
