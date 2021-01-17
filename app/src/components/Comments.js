import React from 'react';

// css
import './Comments.css';

const Comments = ({ comments }) => {
    return (
        <div className="comments-container">
            {comments}
        </div>
    );
}

export default Comments;
