import { Fragment, useState, useContext } from "react";
import RegisterForm from "./RegisterForm";
import { LoginContext } from "../LoginContext";

export default function LoginForm() {
  const [registerModalStatus, setRegisterModalStatus] = useState(false);
  const [resetPasswordModalStatus, setResetPasswordModalStatus] =
    useState(false);
  const [loginCredentials, setLoginCredentials] = useState({
    username: "",
    password: "",
  });
  const { setLoginToken } = useContext(LoginContext);

  function handleLogin(event) {
    event.preventDefault();
    fetch("http://127.0.0.1:8000/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginCredentials),
    })
      .then((res) => res.json())
      .then((data) => {
        setLoginToken(data.token);
        console.log(data.token);
      })
      .catch((err) => console.log(err));
  }

  function handleOpenRegisterModal() {
    setRegisterModalStatus((prevModalStatus) => {
      return !prevModalStatus;
    });
  }

  function handleLoginInput(event) {
    const { name, value } = event.target;
    setLoginCredentials((prevLoginCredentials) => {
      return {
        ...prevLoginCredentials,
        [name]: value,
      };
    });
  }

  return (
    <Fragment>
      <div className="login-container">
        <form className="login-form">
          <input
            type="text"
            placeholder="username"
            name="username"
            id="username"
            value={loginCredentials.username}
            onChange={handleLoginInput}
          />
          <input
            type="password"
            placeholder="password"
            name="password"
            id="password"
            value={loginCredentials.password}
            onChange={handleLoginInput}
          />
          <button
            type="submit"
            className="login-btn"
            onClick={(event) => handleLogin(event)}
          >
            Log in
          </button>
          <p className="reset-password-link">Forgotten Password?</p>
        </form>
        <div>
          <button
            type="button"
            className="create-account-btn"
            onClick={handleOpenRegisterModal}
          >
            Create new Account
          </button>
        </div>
      </div>
      {registerModalStatus && (
        <RegisterForm
          registerModalStatus={registerModalStatus}
          handleOpenRegisterModal={handleOpenRegisterModal}
        />
      )}
    </Fragment>
  );
}
