import { useContext } from "react";
import { Link } from "react-router-dom";
import { LoginContext } from "../LoginContext";

export default function Header() {
  const { loginToken } = useContext(LoginContext);

  return (
    <div className="header-container">
      <Link to="" className="navbar-link">
        <h1>FilmExplorer</h1>
      </Link>

      <input
        type="text"
        placeholder="Search Movie"
        className="movie-searchbar"
      />
      <button className="find-movie-btn">Search</button>
      <div className="navbar-container">
        <ul className="navbar-option">
          <li>
            <Link to="login" className="navbar-link">
              <p>{loginToken ? "Hello / Log Out" : "Register / Sign In"}</p>
            </Link>
          </li>
        </ul>
      </div>
    </div>
  );
}
