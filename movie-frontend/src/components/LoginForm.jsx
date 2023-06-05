export default function LoginForm() {
  return (
    <div className="login-container">
      <form className="login-form">
        <label htmlFor="username">
          <strong>Username: </strong>
        </label>
        <input
          type="text"
          placeholder="username"
          name="username"
          id="username"
        />
        <label htmlFor="password">
          <strong>Password: </strong>
        </label>
        <input
          type="text"
          placeholder="password"
          name="password"
          id="password"
        />
        <button type="submit">Log in</button>
      </form>
      <p>Forgotten Password?</p>
      <div>
        <button type="button">Create new Account</button>
      </div>
    </div>
  );
}
