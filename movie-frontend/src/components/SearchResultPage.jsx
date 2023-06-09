import { useContext } from "react";
import { SearchContext } from "../SearchContext";

export default function SearchPage() {
  const { searchOutput } = useContext(SearchContext);
  console.log(searchOutput);

  return (
    <div className="result-page">
      {searchOutput ? (
        <div className="result-details">
          <h1>{searchOutput.title}</h1>
          <div className="result-movie-description">
            <p>
              An ancient struggle between two Cybertronian races, the heroic
              Autobots and the evil Decepticons, comes to Earth, with a clue to
              the ultimate power held by a teenager.
            </p>
          </div>
          <div className="result-movie-info">
            <p>
              <strong>Genre: </strong>
              {searchOutput.genre}
            </p>
            <p>
              <strong>Language: </strong>
              {searchOutput.language}
            </p>
            <p>
              <strong>Length: </strong>
              {searchOutput.duration} minutes
            </p>
            <p>
              <strong>Director: </strong>
              {searchOutput.director.name}
            </p>
            <span>
              <strong>Actors: </strong>
              {searchOutput.actors.map((actor) => {
                return (
                  <p key={actor.id} className="result-actor-name">
                    {actor.name},
                  </p>
                );
              })}
            </span>
          </div>
        </div>
      ) : (
        <p>Loading</p>
      )}
    </div>
  );
}
