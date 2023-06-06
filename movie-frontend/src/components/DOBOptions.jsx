export default function DOBOptions(props) {
  const currrentYear = new Date().getFullYear();

  return (
    <div className="dob-container">
      <div className="dob-day-container">
        <select
          name="day"
          value={props.dateOfBirth.day}
          onChange={props.handleDOB}
          required
        >
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
        <select
          name="month"
          value={props.dateOfBirth.month}
          onChange={props.handleDOB}
          required
        >
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
        <select
          name="year"
          value={props.dateOfBirth.year}
          onChange={props.handleDOB}
          required
        >
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
