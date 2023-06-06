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
        <label>
          Day
          <select value={props.dateOfBirth.day}>
            <option value="">Day</option>
            {Array.from({ length: 31 }, (_, index) => index + 1).map((day) => {
              return (
                <option key={day} value={day}>
                  {day}
                </option>
              );
            })}
          </select>
        </label>
      </div>
      <div className="dob-month-container">
        <label>
          Month
          <select value={props.dateOfBirth.month}>
            <option value="">Month</option>
            {Array.from({ length: 12 }, (_, index) => index + 1).map(
              (month) => {
                return (
                  <option key={month} value={month}>
                    {month}
                  </option>
                );
              }
            )}
          </select>
        </label>
      </div>
      <div className="dob-year-container">
        <label>Year</label>
        <select value={props.dateOfBirth.year}>
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
