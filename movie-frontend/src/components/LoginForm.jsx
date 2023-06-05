export default function LoginForm() {
  function handleLogin(event) {
    event.preventDefault();
  }

  return (
    <div className="login-container">
      <form className="login-form">
        <input
          type="text"
          placeholder="username"
          name="username"
          id="username"
        />
        <input
          type="text"
          placeholder="password"
          name="password"
          id="password"
        />
        <button
          type="submit"
          className="login-btn"
          onClick={(event) => handleLogin(event)}
        >
          Log in
        </button>
        <p>Forgotten Password?</p>
      </form>
      <div>
        <button type="button" className="register-btn">
          Create new Account
        </button>
      </div>
    </div>
  );
}
