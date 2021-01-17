import React , { useState, useEffect }from 'react';

// import chart component
import { Doughnut } from "react-chartjs-2";

// css
import "./PieChart.css";

const PieChart = ({ticker, setTicker, currentDashboard, setCurrentDashboard}) => {

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
                let labels= []
                let values = []
                let borderColors = []
                let backgroundColors = []
                res.slice(0, 10).map((stock) => labels.push(stock["ticker"]))
                res.slice(0, 10).map((stock) => values.push(stock["rating"].toString().slice(0,4)))
                res.slice(0, 10).map((stock) => borderColors.push('black'))
                res.slice(0, 10).map((stock) => backgroundColors.push('#52B788'))
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
                        if(item){

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
                {!data? "Loading.." : <Doughnut data={data} options={options} />}
            </div>


        </div>
    );
};

export default PieChart;
