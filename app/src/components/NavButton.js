import React from "react";

// css
import "./NavButton.css";

const NavButton = ({ buttonIndex, rating, popularity, rocketships, yolos }) => {
    if (buttonIndex === 0) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-0">Rating</div>
                <div className="nav-button-text-0">{rating}</div>
            </div>
        );
    } else if (buttonIndex === 1) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-1">Popularity</div>
                <div className="nav-button-text-0">{popularity}</div>
            </div>
        );
    } else if (buttonIndex === 2) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-2">
                    # of <i class="fas fa-rocket"></i>
                </div>
                <div className="nav-button-text-0">{rocketships}</div>
            </div>
        );
    } else if (buttonIndex === 3) {
        return (
            <div className="nav-button-container">
                <div className="nav-button-text-3"># of YOLO's</div>
                <div className="nav-button-text-0">{yolos}</div>
            </div>
        );
    } else {
        return null;
    }
};

export default NavButton;
