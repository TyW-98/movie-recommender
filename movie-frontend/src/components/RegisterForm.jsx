import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmark } from "@fortawesome/free-solid-svg-icons";
import CountryOptions from "./CountryOptions";
import DOBOptions from "./DOBOptions";
import GenderOptions from "./GenderOptions";

export default function RegisterForm(props) {
  const [accountCreated, setAccountCreated] = useState(false);
  const [countryObject, setCountryObject] = useState();
  const [registerDetails, setRegisterDetails] = useState({
    email: "",
    username: "",
    password: "",
    password2: "",
    preferredName: "",
    dob: {
      day: "",
      month: "",
      year: "",
    },
    gender: "",
    country: "",
  });

  const formElements = [
    { label: "Email", name: "email", id: "email" },
    { label: "Username", name: "username", id: "register-username" },
    { label: "Password", name: "password", id: "register-password" },
    { label: "Confirmation Password", name: "password2", id: "password2" },
    { label: "Preferred Name", name: "preferredName", id: "preferred-name" },
    { label: "Date of Birth", name: "dob", id: "dob" },
    { label: "Gender", name: "gender", id: "gender" },
    { label: "Country", name: "country", id: "country" },
  ];

  function registerNewUser(event) {
    event.preventDefault();
    console.log(registerDetails);
    fetch("http://127.0.0.1:8000/api/users/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(registerDetails),
    })
      .then((res) => res.json())
      .then(() => props.handleOpenRegisterModal())
      .catch((err) => console.log(err));
  }

  function handleRegisterDetails(event) {
    const { name, value } = event.target;
    setRegisterDetails((prevRegisterDetails) => {
      return {
        ...prevRegisterDetails,
        [name]: value,
      };
    });
  }

  function handleSelectedCountry(option) {
    setCountryObject(option);
    setRegisterDetails((prevRegisterDetails) => {
      return {
        ...prevRegisterDetails,
        country: option.value,
      };
    });
  }

  console.log(registerDetails);

  function handleSelectedGender(event) {
    const { value } = event.target;
    setRegisterDetails((prevRegisterDetails) => {
      return {
        ...prevRegisterDetails,
        gender: value,
      };
    });
  }

  function handleDOB(event) {
    const { name, value } = event.target;
    setRegisterDetails((prevRegisterDetails) => {
      return {
        ...prevRegisterDetails,
        dob: {
          ...prevRegisterDetails.dob,
          [name]: value,
        },
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
        <form className="register-form" onSubmit={registerNewUser}>
          {formElements.map((element) => {
            return (
              <div key={element.id}>
                <label htmlFor={element.id}>
                  <strong>{element.label}</strong>
                </label>
                {element.id === "country" ? (
                  <CountryOptions
                    selectedCountry={countryObject}
                    handleSelectedCountry={handleSelectedCountry}
                  />
                ) : element.id === "dob" ? (
                  <DOBOptions
                    dateOfBirth={registerDetails.dob}
                    handleDOB={handleDOB}
                  />
                ) : element.id === "gender" ? (
                  <GenderOptions handleSelectedGender={handleSelectedGender} />
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
                    onChange={handleRegisterDetails}
                    required
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
