import { useState, createContext } from "react";

const LoginContext = createContext();

function LoginProvider(props) {
  const [loginToken, setLoginToken] = useState(null);

  return (
    <LoginContext.Provider value={{ loginToken, setLoginToken }}>
      {props.children}
    </LoginContext.Provider>
  );
}

export { LoginProvider, LoginContext };
