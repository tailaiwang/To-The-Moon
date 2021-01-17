import React, { useState, useEffect } from 'react';

// import chart component
import { Doughnut } from "react-chartjs-2";

// css
import "./PieChart.css";

const PieChart = ({ ticker, setTicker, currentDashboard, setCurrentDashboard }) => {

    const [data, setData] = useState(null);
    const [options, setOptions] = useState(null);

    const getDataReq = {
        method: "GET",
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": true,
        }
    };

    useEffect(() => {
        fetch('/api/ratings', getDataReq)
            .then((results) => results.json()
            )
            .then((res) => {
                const colorScheme = [
                    "#25CCF7", "#FD7272", "#54a0ff", "#00d2d3",
                    "#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e",
                    "#16a085", "#27ae60", "#2980b9", "#8e44ad", "#2c3e50",
                    "#f1c40f", "#e67e22", "#e74c3c", "#ecf0f1", "#95a5a6",
                    "#f39c12", "#d35400", "#c0392b", "#bdc3c7", "#7f8c8d",
                    "#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9",
                    "#00b894", "#00cec9", "#0984e3", "#6c5ce7", "#ffeaa7",
                    "#fab1a0", "#ff7675", "#fd79a8", "#fdcb6e", "#e17055",
                    "#d63031", "#feca57", "#5f27cd", "#54a0ff", "#01a3a4"
                ]

                let labels = []
                let values = []
                let borderColors = []
                let backgroundColors = []
                res.slice(0, 10).map((stock) => labels.push(stock["ticker"]))
                res.slice(0, 10).map((stock) => values.push(stock["rating"].toString().slice(0, 4)))
                res.slice(0, 10).map((stock) => borderColors.push('black'))
                res.slice(0, 10).map((stock) => {
                    backgroundColors.push(colorScheme[Math.floor(Math.random() * colorScheme.length)])
                })
                setData({
                    labels: labels,
                    datasets: [
                        {
                            label: 'Top Bullish Stocks',
                            data: values,
                            borderColor: borderColors,
                            backgroundColor: backgroundColors,
                            pointBackgroundColor: 'black',
                            pointbordercolor: 'black',
                        }
                    ],

                })

                setOptions({

                    onClick: (evt, item) => {
                        console.log(item)
                        if (item.length) {
                            setTicker(labels[item[0]._index])
                            setCurrentDashboard(1)
                        }

                    },
                })
            });
    }, []);





    return (
        <div className="pie-chart-container">
            <h2 className="font-weight-light mt-3">
                🚀 WallStreetBets' Top Stocks 🚀
            </h2>

            <div className="chart-div">
                {!data ? "Loading.." : <Doughnut data={data} options={options} />}
            </div>


        </div>
    );
};

export default PieChart;
