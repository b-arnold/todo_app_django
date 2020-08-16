import React, { useEffect, useState } from "react";
import { render } from "react-dom";

const App = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("api/user")
      .then((response) => {
        if (response.status > 400) {
          console.log(response.status, response.statusText);
        }
        return response.json();
      })
      .then((data) => {
        setUser(data[0]);
      });
  }, []);

  return <div>User is: {user && user.email}</div>;
};

export default App;

const container = document.getElementById("app");
render(<App />, container);
