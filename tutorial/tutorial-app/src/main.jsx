import React from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import Footer from "./components/footer.jsx";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "test/",
    element: <Footer />,
  },
]);

export const Context = React.createContext();

const animals = ["horse", "dog", "cat", "lion", "Tiger"];

const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <Context.Provider value={{ animals: animals }}>
      <RouterProvider router={router} />
    </Context.Provider>
  </React.StrictMode>
);
