import React from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";
import { MovieConsumer } from "./MovieContext.jsx";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
