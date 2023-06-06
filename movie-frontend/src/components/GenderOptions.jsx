export default function GenderOptions(props) {
  const genders = ["male", "female", "other"];

  return (
    <div className="gender-container">
      {genders.map((gender) => {
        return (
          <div className="gender-option" key={gender}>
            <label htmlFor={gender}>
              {gender.charAt(0).toUpperCase() + gender.slice(1)}
            </label>
            <input
              type="radio"
              name="gender"
              value={gender}
              id={gender}
              onClick={props.handleGender}
              required
            />
          </div>
        );
      })}
    </div>
  );
}
