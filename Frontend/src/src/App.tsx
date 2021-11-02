import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div className="App-form">
        <p className=".App-header">Upload PDF</p>
        <form action="/action_page.php">
          <input type="file" id="myFile" name="filename" />
          <input type="submit" />
        </form>
      </div>
    </div>
  );
}

export default App;
