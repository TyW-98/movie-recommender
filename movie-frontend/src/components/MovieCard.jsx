export default function MovieCard(props) {
  return (
    <div className="movie-card-container">
      <h5>
        {props.title}({props.publishedDate})
      </h5>
      <p>{props.metaScore}</p>
    </div>
  );
}
