import React from 'react';
// import logo from ''

// css
import './Search.css';

const Search = ({ logo, search, setSearch, ticker, setTicker }) => {

    const clickHandler = (e) => {
        setSearch("");
    }

    const searchHandler = (e) => {
        setSearch(e.target.value);
    }

    // const submitSearchHandler = (e) => {
    //     e.preventDefault();
    //     setSearch("");
    // }

    const submitHandler = (e) => {
        setTicker(search);
        e.preventDefault();
    }

    return(
        <div className="nav-div">
            <div className="logo">
                <img className="logo-img" src={logo} alt=""/>
            </div>


            <form>
                <input 
                    type="text" 
                    value={search}
                    onClick={clickHandler}
                    onChange={searchHandler}  
                    className="search-input"
                />
                
                <button className="ghost-button" onClick={submitHandler}>
                </button>
            </form>


            {/* <div className="search-bar">
                <div className="search-text">
                    Hello Fuckers
                </div>
            </div> */}
        </div>
    )
}

export default Search;

//onClick={clickHandler} input
//onClick={submitSearchHandler} button