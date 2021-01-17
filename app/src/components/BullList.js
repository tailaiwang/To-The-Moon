import React, { useState, useEffect } from 'react';

// import logo from ''

// css
import './BullList.css';

const BullList = ({ currentDashboard, setCurrentDashboard, ticker, setTicker }) => {

    const [data, setData] = useState(null);

    const getDataReq = {
        method: "GET",
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": true,
        }
    };

    useEffect(() => {
        fetch('/api/tickers', getDataReq)
            .then(results => results.json())
            .then(data => {
                setData(data);
            });
    }, []);

    const displayTopStocks = () => {
        return (
            <div className="container mt-3">
                <div className="list-group">
                    {data.slice(0, 10).map((stock, index) => (
                        <button type="button " onClick={() => {setTicker(stock); setCurrentDashboard(1)}} className="list-group-item list-group-item-action">{index % 2 == 0? '🚀' : '📈'}{stock}</button>
                    ))}
                </div>
            </div>

        );
    }

    return (
        <>
            <div className="bull-list-container">
                <h2 className = "mt-3">
                    List of Top Bullish Stocks based on Market Sentiment Analysis
                </h2>
            
                   {!data ? 'Loading...' : displayTopStocks()}
                
            </div>
        </>
    );
}

export default BullList;