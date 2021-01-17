import React from "react";

// import chart component
import { Doughnut } from "react-chartjs-2";

// css
import "./PieChart.css";

const PieChart = () => {
    const data = {
        labels: ["$TSLA", "$PLTR", "$GME", "Other"],
        datasets: [
            {
                label: "Top Bullish Stocks",
                data: [4, 3, 2, 1],
                borderColor: ["black", "black", "black", "black"],
                backgroundColor: ["#52B788", "#52B788", "#52B788", "#52B788"],
                pointBackgroundColor: "black",
                pointbordercolor: "black",
            },
        ],
    };

    return (
        <div className="pie-chart-container">
            <div className="pie-title">🚀 WallStreetBets' Top Stocks 🚀</div>

            <div className="chart-div">
                <Doughnut data={data} />
            </div>
        </div>
    );
};

export default PieChart;
