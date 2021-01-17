import React, { useState, useEffect } from "react";

// css
import "./Dashboard.css";

// components
import SideNav from "./SideNav.js";
import BullList from "./BullList.js";
import PieChart from "./PieChart.js";
import Comments from "./Comments.js";

const Dashboard = ({
    currentDashboard,
    setCurrentDashboard,
    setTicker,
    ticker,
}) => {
    const [rating, setRating] = useState(0);
    const [popularity, setPopularity] = useState(0);
    const [rocketships, setRocketships] = useState(0);
    const [yolos, setYolos] = useState(0);
    const [comments, setComments] = useState("");

    const getDataReq = {
        method: "GET",
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": true,

        },
    };

    useEffect(() => {
        if (ticker) {
            console.log(ticker);
            fetch(`/api/ratings/${ticker}`, getDataReq)
                .then((results) => {
                    console.log(results)
                    return results.json()
                })
                .then((data) => {
                    if (data.description === undefined) {
                        data.description = "";
                    }
                    console.log(data);
                    setRating(data.rating);
                    setPopularity(data.score);
                    setRocketships(data.title.concat(data.description).concat(data.comments).match(/🚀/g || []).length);
                    setYolos((data.flairs.match(/YOLO/g) || []).length);
                    setComments(data.comments);
                });
        }
    }, [ticker]);

    if (currentDashboard === 0) { // main dashboard
        return (
            <div>
                <BullList currentDashboard={currentDashboard} setCurrentDashboard={setCurrentDashboard} setTicker={setTicker} ticker={ticker} />
                <PieChart setTicker={setTicker} ticker={ticker} currentDashboard={currentDashboard} setCurrentDashboard={setCurrentDashboard} />
            </div>
        );
    } else if (currentDashboard === 1) { // individual ticker
        return (
            <div>
                <div className="current-ticker">
                    <div className="current-ticker-text">
                        Current Ticker: <br></br>
                        {ticker}
                    </div>
                </div>
                <SideNav
                    rating={rating}
                    popularity={popularity}
                    rocketships={rocketships}
                    yolos={yolos}
                />
                <Comments
                    comments={comments}
                />
            </div>
        );
    }
};

export default Dashboard;
