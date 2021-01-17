import React from 'react';

// css
import './SideNav.css'

// components
import NavButton from './NavButton';

const SideNav = ({ currentDashboard, setCurrentDashboard }) => {
    return(
        <div className="nav-container">
            <div className="nav-list">
                <div>
                    <NavButton 
                        buttonIndex={0}
                        currentDashboard={currentDashboard}
                        setCurrentDashboard={setCurrentDashboard}

                    />
                </div>
                <div>
                    <NavButton 
                        buttonIndex={0}
                        currentDashboard={currentDashboard}
                        setCurrentDashboard={setCurrentDashboard}

                    />
                </div>
                <div>
                    <NavButton 
                        buttonIndex={0}
                        currentDashboard={currentDashboard}
                        setCurrentDashboard={setCurrentDashboard}

                    />
                </div>
                <div>
                    <NavButton 
                        buttonIndex={0}
                        currentDashboard={currentDashboard}
                        setCurrentDashboard={setCurrentDashboard}

                    />
                </div>
            </div>
        </div>
    );
}

export default SideNav;