import React, { useState } from 'react';
import axios from 'axios';
import './RandomContent.css'; 

const RandomContent = () => {
  const [joke, setJoke] = useState('');

  const fetchContent = async () => {
    try {
      const response = await axios.get('https://official-joke-api.appspot.com/random_joke');
      
      const fullJoke = `${response.data.setup} ${response.data.punchline}`;
      setJoke(fullJoke);
    } catch (error) {
      console.error("Error fetching content:", error);
      setJoke("Failed to fetch content.");
    }
  };

  return (
    <div className="container">
      <button className="button" onClick={fetchContent}>
        Generate JOKE
      </button>
      {joke && (
        <div className="content-box">
          <p className="quote">"{joke}"</p>
        </div>
      )}
    </div>
  );
};

export default RandomContent;
