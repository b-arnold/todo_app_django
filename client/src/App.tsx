import React, { useState, useEffect } from "react";
import "./App.css";

interface User {
  email: string;
}

function App() {
  const [user, setUser] = useState<User>({ email: "" });

  useEffect(() => {
    fetch("/api/user")
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setUser(data[0]);
      });
  }, []);

  return (
    <div className="App">
      <p>User: {user && user.email}</p>
    </div>
  );
}

export default App;
