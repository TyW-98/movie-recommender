import { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faStar } from "@fortawesome/free-solid-svg-icons";
import YouTube from "react-youtube";

export default function MovieCard(props) {
  const [expanded, setExpanded] = useState(false);
  const [movieDetails, setMovieDetails] = useState();
  const [hoverRating, setHoverRating] = useState(0);
  const [userRating, setUserRating] = useState(props.currentMovieUserRating);

  function handleExpansion() {
    setExpanded((prevExpanded) => !prevExpanded);
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

  function sendUserRating(newRating) {
    fetch(`http://127.0.0.1:8000/api/movies/${props.id}/rate_movie/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token c1abe057feb15cd89090a4c6221381a0851769e3",
      },
      body: JSON.stringify({ rating: newRating }),
    })
      .then((res) => res.json())
      .then((res) => {
        setUserRating(newRating);
        props.handleUpdateUserRatings();
      })
      .catch((err) => console.log(err));
  }

  function handleStar(event, starIdx) {
    if (event.type === "mouseenter") {
      setHoverRating(starIdx + 1);
    } else if (event.type === "mouseleave") {
      setHoverRating(-1);
    } else if (event.type === "click") {
      if (props.currentMovieUserRating === starIdx + 1) {
        sendUserRating(0);
        props.handleUpdateUserRatings();
        return 0;
      } else {
        sendUserRating(starIdx + 1);
        props.handleUpdateUserRatings();
        return starIdx + 1;
      }
    }
  }

  const displayRating = hoverRating > 0 ? hoverRating : userRating;

  return (
    <div className="movie-card-container">
      <div>
        <div className="movie-card-main">
          <div className="movie-card-header">
            <span className="card-expand-control" onClick={handleExpansion}>
              {expanded ? "▲" : "▼"}
            </span>
            <h5>{props.title}</h5>
          </div>
          <div>
            {[...Array(5)].map((_, index) => {
              return (
                <FontAwesomeIcon
                  key={index}
                  icon={faStar}
                  style={{
                    color: index < displayRating ? "#f5c211" : "#142227",
                    cursor: "pointer",
                  }}
                  onClick={(event) => handleStar(event, index)}
                  onMouseEnter={(event) => handleStar(event, index)}
                  onMouseLeave={(event) => handleStar(event, index)}
                />
              );
            })}
          </div>
        </div>
      </div>
      {expanded && (
        <div className="movie-card-descriptions">
          <YouTube videoId={"itnqEauWQZM"} />
          {movieDetails && (
            <div className="movie-card-details">
              <div className="movie-description">
                <p>
                  An ancient struggle between two Cybertronian races, the heroic
                  Autobots and the evil Decepticons, comes to Earth, with a clue
                  to the ultimate power held by a teenager.
                </p>
              </div>
              <div className="movie-info">
                <p>
                  <strong>Genre: </strong>
                  {movieDetails.genre}
                </p>
                <p>
                  <strong>Released Date: </strong>
                  {props.publishedDate}
                </p>
                <p>
                  <strong>Language: </strong>
                  {movieDetails.language}
                </p>
                <p>
                  <strong>Length: </strong>
                  {movieDetails.duration} minutes
                </p>
                <p>
                  <strong>Director: </strong>
                  {movieDetails.director.name}
                </p>
                <span className="actor-name-list">
                  <strong>Actors: </strong>
                  {movieDetails.actors.map((actor) => {
                    return (
                      <p key={actor.id} className="actor-name">
                        {actor.name},
                      </p>
                    );
                  })}
                </span>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
