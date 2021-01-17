import React from "react";

// css
import "./NavButton.css";

const NavButton = ({ buttonIndex, rating, popularity, rocketships, yolos }) => {
    if (buttonIndex === 0) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-0">Rating</div>
                <strong>{rating.toFixed(2)}</strong>
            </div>
        );
    } else if (buttonIndex === 1) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-1">Popularity</div>
                <strong>{popularity}</strong>
            </div>
        );
    } else if (buttonIndex === 2) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-2">
                    # of <i className="fas fa-rocket"></i>
                </div>
                <strong>{rocketships}</strong>
            </div>
        );
    } else if (buttonIndex === 3) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-3"># of YOLO's</div>
                <strong>{yolos}</strong>
            </div>
        );
    } else {
        return null;
    }
};

export default NavButton;
