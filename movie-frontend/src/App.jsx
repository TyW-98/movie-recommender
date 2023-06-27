import { Fragment } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import "flag-icons/css/flag-icons.min.css";
import Header from "./components/Header.jsx";
import MovieCardSection from "./components/MovieCardSection";
import LoginForm from "./components/LoginForm";
import SearchPage from "./components/SearchResultPage";
import { LoginProvider } from "./LoginContext";
import { SearchProvider } from "./SearchContext";
import Footebar from "./components/Footerbar";

export default function App() {
  return (
    <Fragment>
      <Router>
        <LoginProvider>
          <SearchProvider>
            <Header />
            <div className="main-content">
              <Routes>
                <Route path="/" element={<MovieCardSection />} />
                <Route path="/login" element={<LoginForm />} />
                <Route path="/result" element={<SearchPage />} />
              </Routes>
            </div>
            <Footebar />
          </SearchProvider>
        </LoginProvider>
      </Router>
    </Fragment>
  );
}
