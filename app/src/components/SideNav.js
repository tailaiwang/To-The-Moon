import React from "react";

// css
import "./SideNav.css";

// components
import NavButton from "./NavButton";

const SideNav = ({ currentDashboard, setCurrentDashboard }) => {
    return (
        <div className="nav-container">
            <div className="nav-list">
                <div>
                    <NavButton buttonIndex={0} />
                </div>
                <div>
                    <NavButton buttonIndex={1} />
                </div>
                <div>
                    <NavButton buttonIndex={2} />
                </div>
                <div>
                    <NavButton buttonIndex={3} />
                </div>
            </div>
        </div>
    );
};

export default SideNav;
