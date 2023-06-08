import { useState, useEffect, Fragment, useContext } from "react";
import MovieCard from "./MovieCard";
import PuffLoader from "react-spinners/PuffLoader";
import { LoginContext } from "../LoginContext";

export default function MoiveCardSection() {
  const [movieData, setMovieData] = useState([]);
  const [userRatings, setUserRatings] = useState();
  const [updateUserRatings, setUpdateUserRatings] = useState(true);
  const [isLoading, setIsLoading] = useState(true);

  const { loginToken } = useContext(LoginContext);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/movies/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token 015f83c9038216e9fc85d3643f9fc70dc5de368d", // Admin Token
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
        setMovieData(filteredData);
      });
  }, []);

  useEffect(() => {
    if (updateUserRatings) {
      setIsLoading(true);
      fetch("http://127.0.0.1:8000/api/users/user_rated_movies/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token c1abe057feb15cd89090a4c6221381a0851769e3", // User 4 Token
        },
      })
        .then((res) => res.json())
        .then((data) => {
          setUserRatings(data);
        })
        .then(() => setUpdateUserRatings(false))
        .then(() => setIsLoading(false))
        .catch((err) => console.log(err));
    }
  }, [updateUserRatings]);

  function handleUpdateUserRatings() {
    setUpdateUserRatings(true);
  }

  return (
    <Fragment>
      {isLoading && !userRatings ? (
        <div className="loader-container">
          <div className="loader-component">
            <PuffLoader color="#132d6e" size={80} />
          </div>
        </div>
      ) : (
        <div className="movies-section">
          {movieData.map((movie) => {
            const currentMovieUserRating =
              userRatings.output.find(
                (ratedMovie) => ratedMovie.movie === movie.id
              )?.user_rating ?? 0;
            return (
              <MovieCard
                id={movie.id}
                key={movie.id}
                title={movie.title}
                publishedDate={movie.publishedDate}
                avgRating={movie.averageRating}
                currentMovieUserRating={
                  !userRatings ? 0 : currentMovieUserRating
                }
                handleUpdateUserRatings={handleUpdateUserRatings}
              />
            );
          })}
        </div>
      )}
    </Fragment>
  );
}
