import React, { useState, useEffect } from 'react';
import './App.css';

// import components
import Search from './components/Search.js';
import SideNav from './components/SideNav.js';
import Chart from './components/Chart.js';

// import assets
import logo from './assets/Swing.png';



function App() {
  // app states
  // states
  const [search, setSearch] = useState("Enter a ticker...");
  const [ticker, setTicker] = useState("");


  return (
    <div className="App">

      <header className="App-header">
        <Search 
          logo={logo}
          search={search}
          setSearch={setSearch}
          ticker={ticker}
          setTicker={setTicker}
        />
      </header>

      <div className="page-container">

        <SideNav

        />

        <Chart
          ticker={ticker}
        />

      </div>

    </div>
  );
}

export default App;
