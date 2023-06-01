export default function Header() {
  return (
    <div className="header-container">
      <h1>FilmExplorer</h1>
      <input
        type="text"
        placeholder="Search Movie"
        className="movie-searchbar"
      />
      <button className="find-movie-btn">Search</button>
      <div className="navbar-container">
        <ul className="navbar-option">
          <li>
            <p>Movie List</p>
          </li>
          <li>
            <p>Sign In</p>
          </li>
        </ul>
      </div>
    </div>
  );
}
