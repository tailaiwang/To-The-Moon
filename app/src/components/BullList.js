import React, { useState, useEffect } from 'react';

// import logo from ''

// css
import './BullList.css';

const BullList = () => {

    const [ data, setData ] = useState(null);

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

    return(
        <>
            <div className="bull-list-container">
                <p>
                    List of Top Bullish Stocks based on Market Sentiment Analysis
                </p>
                <p>
                    Data: {!data ? 'Loading...' : `${data}`}
                </p>
            </div>
        </>
    );
}

export default BullList;