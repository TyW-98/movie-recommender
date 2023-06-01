import { createContext } from "react";

const { Provider, Consumer } = createContext();

function MovieProvider(props) {
  return <Provider>{props.children}</Provider>;
}

export { MovieProvider, Consumer as MovieConsumer };
