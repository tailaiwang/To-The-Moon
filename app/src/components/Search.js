import React from "react";
// import logo from ''

// css
import "./Search.css";

const Search = ({
    logo,
    search,
    setSearch,
    ticker,
    setTicker,
    currentDashboard,
    setCurrentDashboard,
}) => {
    const dashboardHandler = (e) => {
        setCurrentDashboard(0);
    };

    const clickHandler = (e) => {
        setSearch("");
    };

    const searchHandler = (e) => {
        setSearch(e.target.value);
    };

    const submitHandler = (e) => {
        setCurrentDashboard(1);
        setTicker(search);
        e.preventDefault();
    };

    return (
        <div className="nav-div">
            <div className="logo" onClick={dashboardHandler}>
                {/* <img className="logo-img" src={logo} alt=""/> */}
                <i className="fas fa-chart-line logo-img"></i>
                <div className="title">To The Moon 🚀</div>
            </div>
            <form>
                <input
                    type="text"
                    value={search}
                    onClick={clickHandler}
                    onChange={searchHandler}
                    className="search-input"
                />
                <button className="ghost-button" onClick={submitHandler}></button>
            </form>
        </div>
    );
};

export default Search;
