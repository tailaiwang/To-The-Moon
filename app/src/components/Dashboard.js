import React from 'react';

// css
import './Dashboard.css'

// components
import SideNav from './SideNav.js';
import Chart from './Chart.js';
import BullList from './BullList.js';
import PieChart from './PieChart.js';
import Comments from './Comments.js';

const Dashboard = ({ currentDashboard, 
    setCurrentDashboard, 
    ticker }) => {

    if (currentDashboard === 0) {
        return(
            <div>
                <BullList />
                <PieChart />
            </div>

        )
    }

    else if (currentDashboard === 1) {
        return(
            <div>

                <div className="current-ticker">
                    <div className="current-ticker-text">
                        Current Ticker: <br></br>
                        {ticker}
                    </div>
                </div>
                <SideNav
                    currentDashboard={currentDashboard}
                    setCurrentDashboard={setCurrentDashboard}
                />

                <Comments

                />
            </div>
        );
    }
}

export default Dashboard;