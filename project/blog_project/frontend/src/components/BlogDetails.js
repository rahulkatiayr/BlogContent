import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams, Link } from "react-router-dom";
import "./BlogList.css"; 

const BlogDetail = () => {
  const { id } = useParams(); 
  const [post, setPost] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/posts/${id}/`)
      .then(response => {
        setPost(response.data);
      })
      .catch(error => {
        console.error("Error fetching post detail:", error);
      });
  }, [id]);

  if (!post) {
    return <p>Loading...</p>;
  }

  return (
    <div className="blog-detail">
      <Link to="/" className="back-link">← Back to Posts</Link>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
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
    </div>
  );
};

export default BlogDetail;
