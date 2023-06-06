import { Fragment } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import "flag-icons/css/flag-icons.min.css";
import Header from "./components/Header.jsx";
import MovieCardSection from "./components/MovieCardSection";
import LoginForm from "./components/LoginForm";
import { LoginProvider } from "./LoginContext";

export default function App() {
  return (
    <Fragment>
      <Router>
        <LoginProvider>
          <Header />
          <div className="main-content">
            <Routes>
              <Route path="/" element={<MovieCardSection />} />
              <Route path="/login" element={<LoginForm />} />
            </Routes>
          </div>
        </LoginProvider>
      </Router>
    </Fragment>
  );
}
