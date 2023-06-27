import { useContext } from "react";
import { Link } from "react-router-dom";
import { LoginContext } from "../LoginContext";
import { SearchContext } from "../SearchContext";

export default function Header() {
  const { loginToken, setLoginToken } = useContext(LoginContext);
  const { searchInput, handleSearchInput, handleSearch } =
    useContext(SearchContext);

  function handleLogout() {
    setLoginToken((prevLoginToken) => {
      if (prevLoginToken) {
        window.location.reload();
        return null;
      }
      return prevLoginToken;
    });
  }

  return (
    <div className="header-container">
      <Link to="/" className="navbar-link">
        <h1>FilmExplorer</h1>
      </Link>

      <input
        type="text"
        placeholder="Search Movie"
        className="movie-searchbar"
        value={searchInput}
        onChange={handleSearchInput}
      />
      <button className="find-movie-btn" onClick={() => handleSearch()}>
        Search
      </button>
      <div className="navbar-container">
        <ul className="navbar-option">
          <li>
            <Link to={loginToken ? "/" : "/login"} className="navbar-link">
              <p onClick={handleLogout}>
                {loginToken ? "Hello / Log Out" : "Register / Sign In"}
              </p>
            </Link>
          </li>
        </ul>
      </div>
    </div>
  );
}
