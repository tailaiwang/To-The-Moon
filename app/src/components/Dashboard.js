import React from 'react';

// components
import SideNav from './SideNav.js';
import Chart from './Chart.js';
import BullList from './BullList.js';
import PieChart from './PieChart.js';


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
                <SideNav
                    currentDashboard={currentDashboard}
                    setCurrentDashboard={setCurrentDashboard}
                />

                <Chart
                    ticker={ticker}
                />
            </div>
        );
    }
}

export default Dashboard;