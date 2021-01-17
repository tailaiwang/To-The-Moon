import React, { useState } from "react";
import "./App.css";

// import components
import Search from "./components/Search.js";
import Dashboard from "./components/Dashboard.js";

// import assets
import logo from "./assets/Swing.png";

function App() {
  // search and ticker states
  const [search, setSearch] = useState("Enter a ticker...");
  const [ticker, setTicker] = useState("");

  // nav control states
  const [currentDashboard, setCurrentDashboard] = useState(0);

  return (
    <div className="App">
      <header className="App-header">
        <Search
          logo={logo}
          search={search}
          setSearch={setSearch}
          ticker={ticker}
          setTicker={setTicker}
          currentDashboard={currentDashboard}
          setCurrentDashboard={setCurrentDashboard}
        />
      </header>

      <div className="page-container">
        <Dashboard
          currentDashboard={currentDashboard}
          setCurrentDashboard={setCurrentDashboard}
          ticker={ticker}
          setTicker={setTicker}
        />
      </div>
    </div>
  );
}

export default App;
