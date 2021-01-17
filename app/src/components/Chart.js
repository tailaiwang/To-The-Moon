import React from 'react';

// chart library imports
import { Line } from 'react-chartjs-2'

// css
import './Chart.css';


const Chart = ({ ticker }) => {

    const data = {
        labels: ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
        datasets: [
            {
                label: ticker,
                data: [1, 2, 3, 5, 0, 10, 15, 7],
                borderColor: ['#52B788'],
                backgroundColor: ['rgba(66, 188, 66, 0)'],
                pointBackgroundColor: 'black',
                pointbordercolor: 'black'

            }
        ]
    }

    return(
        <div className="chart-container">
            <Line data={data} />
            {/* HUGE FUCKIN CHART BUD
            <br/>
            <br/>
            <br/>

            displaying: {ticker} */}
        </div>
    );
}

export default Chart;