export default function DOBOptions(props) {
  const currrentYear = new Date().getFullYear();

  function handleDOB(event) {
    const { name, value } = event.target;
    props.setDateOfBirth((prevDateOfBirth) => {
      return {
        ...prevDateOfBirth,
        [name]: value,
      };
    });
  }
  return (
    <div className="dob-container">
      <div className="dob-day-container">
        <select value={props.dateOfBirth.day} onChange={handleDOB}>
          <option value="">Day</option>
          {Array.from({ length: 31 }, (_, index) => index + 1).map((day) => {
            return (
              <option key={day} value={day}>
                {day}
              </option>
            );
          })}
        </select>
      </div>
      <div className="dob-month-container">
        <select value={props.dateOfBirth.month} onChange={handleDOB}>
          <option value="">Month</option>
          {Array.from({ length: 12 }, (_, index) => index + 1).map((month) => {
            return (
              <option key={month} value={month}>
                {month}
              </option>
            );
          })}
        </select>
      </div>
      <div className="dob-year-container">
        <select value={props.dateOfBirth.year} onChange={handleDOB}>
          <option value="">Year</option>
          {Array.from({ length: 100 }, (_, index) => currrentYear - index).map(
            (year) => {
              return (
                <option key={year} value={year}>
                  {year}
                </option>
              );
            }
          )}
        </select>
      </div>
    </div>
  );
}
