import React, { useState, useEffect } from "react";
import axios from "axios";
import "./BlogList.css"; 
import RandomContent from "./RandomContent"; 
import BlogPostItem from "./BlogPostitem"; 

const BlogList = () => {
  const [posts, setPosts] = useState([]);
  const [searchId, setSearchId] = useState(""); 
  const [filteredPost, setFilteredPost] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/posts/")  
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => {
        console.error("Error fetching posts:", error);
      });
  }, []);

  const handleSearch = () => {
    if (!searchId.trim()) {
      setFilteredPost(null);
      return;
    }
    axios.get(`http://127.0.0.1:8000/posts/${searchId}/`)
      .then(response => {
        setFilteredPost(response.data);
      })
      .catch(error => {
        console.error("Error fetching post:", error);
        setFilteredPost(null);
      });
  };

  return (
    <div className="blog-container">
      <h2>Latest Blog Posts</h2>

      
      <RandomContent />

      
      <div className="search-box">
        <input
          type="number"
          placeholder="Enter Blog ID"
          value={searchId}
          onChange={(e) => setSearchId(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      
      {filteredPost ? (
        <BlogPostItem post={filteredPost} />
      ) : (
        <ul>
          {posts.map(post => (
            <li key={post.id}>
              <BlogPostItem post={post} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default BlogList;
