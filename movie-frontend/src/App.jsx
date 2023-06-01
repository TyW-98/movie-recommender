import { Fragment, useState } from "react";
import "./App.css";
import Header from "./components/Header.jsx";
import MoiveCardSection from "./components/MovieCardSection";

export default function App() {
  return (
    <Fragment>
      <Header />
      <MoiveCardSection />
    </Fragment>
  );
}
