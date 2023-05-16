import React from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
]);

export const Context = React.createContext();

const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <Context.Provider>
      <RouterProvider router={router} />
    </Context.Provider>
  </React.StrictMode>
);
