import React from "react";

// css
import "./SideNav.css";

// components
import NavButton from "./NavButton";

const SideNav = ({ rating, popularity, rocketships, yolos }) => {
    return (
        <div className="nav-container">
            <div className="nav-list">
                <div>
                    <NavButton
                        buttonIndex={0}
                        rating={rating}
                        popularity={popularity}
                        rocketships={rocketships}
                        yolos={yolos}
                    />
                </div>
                <div>
                    <NavButton
                        buttonIndex={1}
                        rating={rating}
                        popularity={popularity}
                        rocketships={rocketships}
                        yolos={yolos}
                    />
                </div>
                <div>
                    <NavButton
                        buttonIndex={2}
                        rating={rating}
                        popularity={popularity}
                        rocketships={rocketships}
                        yolos={yolos}
                    />
                </div>
                <div>
                    <NavButton
                        buttonIndex={3}
                        rating={rating}
                        popularity={popularity}
                        rocketships={rocketships}
                        yolos={yolos}
                    />
                </div>
            </div>
        </div>
    );
};

export default SideNav;
