import { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faStar } from "@fortawesome/free-solid-svg-icons";

export default function MovieCard(props) {
  const [expanded, setExpanded] = useState(false);
  const [movieDetails, setMovieDetails] = useState(false);
  const [hoverRating, setHoverRating] = useState(0);
  const [rating, setRating] = useState(0);

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

  function sendUserRating() {
    fetch(`http://127.0.0.1:8000/api/movies/${props.id}/rate_movie/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token c1abe057feb15cd89090a4c6221381a0851769e3",
      },
      body: JSON.stringify({ rating: rating }),
    })
      .then((res) => res.json())
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  }

  function handleStar(event, starIdx) {
    if (event.type === "mouseenter") {
      setHoverRating(starIdx + 1);
    } else if (event.type === "mouseleave") {
      setHoverRating(-1);
    } else if (event.type === "click") {
      setRating((prevRating) => {
        if (prevRating === starIdx + 1) {
          return 0;
        } else {
          return starIdx + 1;
        }
      });
    }
  }

  useEffect(() => {
    const sendRating = setTimeout(sendUserRating, 3000);
    return () => {
      clearTimeout(sendRating);
    };
  }, [rating]);

  const displayRating = hoverRating > 0 ? hoverRating : rating;

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
      {expanded && <div className="movie-card-details"></div>}
    </div>
  );
}
