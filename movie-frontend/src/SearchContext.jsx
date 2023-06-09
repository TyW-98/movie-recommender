import { useState, createContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const SearchContext = createContext();

function SearchProvider(props) {
  const [searchInput, setSearchInput] = useState("");
  const [allMovieData, setAllMovieData] = useState("");
  const [searchOutput, setSearchOutput] = useState("");
  const [isResult, setIsResult] = useState(false);
  const navigate = useNavigate();

  function handleSearchInput(event) {
    const { value } = event.target;
    setSearchInput(value);
  }

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/movies/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        const fetchedData = data.map((movie) => {
          return {
            ...movie,
            publishedDate: movie["published_date"],
            averageRating: movie["average_rating"],
          };
        });
        const keysToRemove = ["published_date", "average_rating"];
        const filteredData = fetchedData.map((movie) => {
          const filteredMovieData = {};
          Object.keys(movie).forEach((key) => {
            if (!keysToRemove.includes(key)) {
              filteredMovieData[key] = movie[key];
            }
          });
          return filteredMovieData;
        });
        setAllMovieData(filteredData);
      });
  }, []);

  function handleSearch() {
    const movieTitle = searchInput.replace(/\+/g, "").toLowerCase();
    const matchingMovie = allMovieData.find(
      (movie) => movie.title.replace(/\+/g, "").toLowerCase() === movieTitle
    );

    console.log(matchingMovie);

    if (matchingMovie) {
      fetch(`http://127.0.0.1:8000/api/movies/${matchingMovie.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          const keysToRemove = ["published_date", "average_rating"];
          const filteredData = {};
          Object.keys(data).forEach((element) => {
            if (!keysToRemove.includes(element)) {
              filteredData[element] = data[element];
            }
          });
          setSearchOutput(filteredData);
          setIsResult(true);
          navigate("/result");
          setSearchInput("");
        })
        .catch((err) => console.log(err));
    } else {
      setIsResult(false);
      navigate("/result");
      setSearchOutput(`No movie with the title ${searchInput} found`);
    }
  }

  return (
    <SearchContext.Provider
      value={{
        searchInput,
        searchOutput,
        isResult,
        handleSearchInput,
        handleSearch,
      }}
    >
      {props.children}
    </SearchContext.Provider>
  );
}

export { SearchProvider, SearchContext };
