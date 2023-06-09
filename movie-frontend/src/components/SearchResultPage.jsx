import { useContext } from "react";
import { SearchContext } from "../SearchContext";

export default function SearchPage() {
  const { searchOutput } = useContext(SearchContext);

  return (
    <div>
      <h1>Testing</h1>
      <p>{searchOutput ? searchOutput.title : "loading"}</p>
    </div>
  );
}
