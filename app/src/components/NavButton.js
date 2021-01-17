import React from 'react';

// css
import './NavButton.css';

const NavButton = ({ buttonIndex,
    currentDashboard,
    setCurrentDashboard  }) => {



    if (buttonIndex == 0) {
        return(
            <div className="nav-button-container">
                <i class="fas fa-chart-bar nav-button-icon"></i>
            </div>
        );
    }
    else if (buttonIndex == 1) {
        return null;
    }
    else if (buttonIndex == 2) {
        return null;
    }
    else {
        return null;
    }
}

export default NavButton;