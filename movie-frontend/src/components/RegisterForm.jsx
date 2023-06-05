export default function RegisterForm() {
  const formElements = [
    { label: "Email", name: "email", id: "email" },
    { label: "Username", name: "username", id: "register-username" },
    { label: "Password", name: "password", id: "register-password" },
    { label: "Confirmation Password", name: "password2", id: "password2" },
    { label: "Preferred Name", name: "preferred_name", id: "preferred-name" },
    { label: "Age", name: "age", id: "age" },
    { label: "Gender", name: "gender", id: "gender" },
    { label: "Country", name: "country", id: "country" },
  ];

  return (
    <div className="register-container">
      <h2>Create a new account</h2>
      <form className="register-form">
        {formElements.map((element) => {
          return (
            <div key={element.id}>
              <label htmlFor={element.id}>
                <strong>{element.label}</strong>
              </label>
              <input type="text" name={element.name} id={element.id} />
            </div>
          );
        })}
      </form>
    </div>
  );
}
