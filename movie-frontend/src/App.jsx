import { Fragment, useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Header from "./components/Header.jsx";
import MovieCardSection from "./components/MovieCardSection";
import LoginForm from "./components/LoginForm";

export default function App() {
  return (
    <Fragment>
      <Router>
        <Header />
        <div className="main-content">
          <Routes>
            <Route path="/" element={<MovieCardSection />} />
            <Route path="/login" element={<LoginForm />} />
          </Routes>
        </div>
      </Router>
    </Fragment>
  );
}
