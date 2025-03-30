import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import "./BlogList.css"; // Re-use your existing CSS

const BlogPostItem = ({ post }) => {
  const [expanded, setExpanded] = useState(false);

  const contentToShow =
    expanded || post.content.length <= 150
      ? post.content
      : post.content.substring(0, 150) + '...';

  const toggleExpanded = () => {
    setExpanded(!expanded);
  };

  return (
    <div className="blog-post">
      <h3>{post.title}</h3>
      <p>{contentToShow}</p>
      {post.content.length > 150 && (
        <button className="details-button" onClick={toggleExpanded}>
          {expanded ? "Show Less" : "Read More"}
        </button>
      )}
      <p className="likes">❤️ Likes: {post.likes}</p>
      <div className="comments-section">
        <h4>Comments</h4>
        {post.comments && post.comments.length > 0 ? (
          <ul>
            {post.comments.map((comment, index) => (
              <li key={index} className="comment">
                <strong>{comment.user}:</strong> {comment.comment}
              </li>
            ))}
          </ul>
        ) : (
          <p>No comments yet.</p>
        )}
      </div>
      
      <Link to={`/posts/${post.id}`} className="view-details-button">
        View Details
      </Link>
    </div>
  );
};

export default BlogPostItem;
