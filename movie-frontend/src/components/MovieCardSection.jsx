import { useState, useEffect, Fragment } from "react";
import MovieCard from "./MovieCard";
import { nanoid } from "nanoid";
import PuffLoader from "react-spinners/PuffLoader";

export default function MoiveCardSection() {
  const [movieData, setMovieData] = useState();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/movies/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token 015f83c9038216e9fc85d3643f9fc70dc5de368d",
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

  return (
    <Fragment>
      {!movieData ? (
        <div className="loader-container">
          <div className="loader-component">
            <PuffLoader color="#132d6e" size={80} />
          </div>
        </div>
      ) : (
        <div className="movies-section">
          {movieData.map((movie) => {
            return (
              <MovieCard
                id={movie.id}
                key={movie.id}
                title={movie.title}
                publishedDate={movie.publishedDate}
                avgRating={movie.averageRating}
              />
            );
          })}
        </div>
      )}
    </Fragment>
  );
}
