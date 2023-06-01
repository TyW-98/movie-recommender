import { useState, useEffect } from "react";
import MovieCard from "./MovieCard";
import { nanoid } from "nanoid";

export default function MoiveCardSection() {
  const [movieData, setMovieData] = useState([
    {
      id: nanoid(),
      title: "Movie 1",
      publishedDate: 2019,
      metaScore: 80,
    },
    {
      id: nanoid(),
      title: "Movie 2",
      publishedDate: 2022,
      metaScore: 66,
    },
  ]);

  // useEffect(() => {
  //   fetch("http://127.0.0.1:8000/api/movies/", {
  //     method: "GET",
  //     headers: {
  //       "Content-Type": "application/json",
  //       Authorization: "Token 015f83c9038216e9fc85d3643f9fc70dc5de368d",
  //     },
  //   })
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setMovieData((data) => {
  //         return data.map((movie) => {
  //           return {
  //             ...movie,
  //             publishedDate: movie["published_date"],
  //             averageRating: movie["average_rating"],
  //           };
  //         });
  //       });
  //     })
  //     .catch((err) => console.log(err));
  // }, []);

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

  console.log(movieData);

  return (
    <div className="movies-section">
      {movieData.map((movie) => {
        return (
          <MovieCard
            key={movie.id}
            title={movie.title}
            publishedDate={movie.publishedDate}
            metaScore={movie.averageRating}
          />
        );
      })}
    </div>
  );
}
