import { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faStar } from "@fortawesome/free-solid-svg-icons";
import YouTube from "react-youtube";

export default function MovieCard(props) {
  const [expanded, setExpanded] = useState(false);
  const [movieDetails, setMovieDetails] = useState(false);
  const [favourite, setFavourite] = useState(false);

  function handleExpansion() {
    setExpanded((prevExpanded) => {
      return !prevExpanded;
    });
  }

  useEffect(() => {
    if (expanded) {
      fetchMovieData();
    }
  }, [expanded]);

  function fetchMovieData() {
    fetch(`http://127.0.0.1:8000/api/movies/${props.id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token 015f83c9038216e9fc85d3643f9fc70dc5de368d",
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
        setMovieDetails(filteredData);
      });
  }

  function toggleFavourite() {
    setFavourite((prevFavourite) => {
      return !prevFavourite;
    });
  }

  return (
    <div className="movie-card-container">
      <div>
        <div className="movie-card-main">
          <div className="movie-card-header">
            <span className="card-expand-control" onClick={handleExpansion}>
              {expanded ? "▲" : "▼"}
            </span>
            <h5>
              {props.title}({props.publishedDate})
            </h5>
          </div>
          <div>
            <FontAwesomeIcon
              icon={faStar}
              style={{ color: favourite ? "#f5c211" : "#142227" }}
              onClick={toggleFavourite}
            />
          </div>
        </div>
      </div>
      {expanded && (
        <div className="movie-card-details">
          <YouTube videoId="v8ItGrI-Ou0" />
        </div>
      )}
    </div>
  );
}
