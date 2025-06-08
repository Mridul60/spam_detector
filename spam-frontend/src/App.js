import React, {useState,useEffect} from 'react';
import axios from 'axios'
import './App.css';

const API_BASE = process.env.REACT_APP_API_BASE|| 'http://localhost:5000';

function App() {
  const [message, setMessage] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  

  // Handle message prediction
  const handlePredict = async () => {
  setLoading(true);
  try {
    const res = await axios.post(`${API_BASE}/predict`, {
      message: message
    });
    setResult(res.data.prediction);
  } catch (err) {
    setResult("Error connecting to backend");
    console.error(err);
  } finally {
    setLoading(false);
  }
};

  const clearMessage = () => {
    setMessage('');
    setResult('');
  };
  // Ping the backend to check if it's running
   useEffect(() => {
    fetch(`${API_BASE}/ping`)
      .then(res => res.json())
      .then(data => console.log("Ping:", data.message))
      .catch(err => console.error("Ping failed:", err));
  }, []);

  return (
    <div className="app">
      <div className="container">
        <div className="header">
          <div className="icon-wrapper">
            <svg className="shield-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L3 7V11C3 16.55 6.84 21.74 12 23C17.16 21.74 21 16.55 21 11V7L12 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M9 12L11 14L15 10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </div>
          <h1 className="title">Spam Classifier</h1>
          <p className="subtitle">Intelligent message filtering powered by AI</p>
        </div>

        <div className="input-section">
          <div className="textarea-wrapper">
            <textarea
              className="message-input"
              placeholder="Enter your message to check if it's spam..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              rows="4"
            />
            {message && (
              <button 
                className="clear-btn"
                onClick={clearMessage}
                aria-label="Clear message"
              >
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
            )}
          </div>
          
          <button 
            className={`predict-btn ${loading ? 'loading' : ''}`}
            onClick={handlePredict} 
            disabled={loading || !message.trim()}
          >
            {loading ? (
              <>
                <div className="spinner"></div>
                <span>Analyzing...</span>
              </>
            ) : (
              <>
                <svg className="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 12L11 14L15 10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                <span>Analyze Message</span>
              </>
            )}
          </button>
        </div>

        {result && (
          <div className={`result-section ${result.toLowerCase().includes('error') ? 'error' : result.toLowerCase()}`}>
            <div className="result-content">
              <div className="result-icon">
                {result.toLowerCase().includes('error') ? (
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="2"/>
                    <line x1="15" y1="9" x2="9" y2="15" stroke="currentColor" strokeWidth="2"/>
                    <line x1="9" y1="9" x2="15" y2="15" stroke="currentColor" strokeWidth="2"/>
                  </svg>
                ) : result.toLowerCase() === 'spam' ? (
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="2"/>
                    <line x1="15" y1="9" x2="9" y2="15" stroke="currentColor" strokeWidth="2"/>
                  </svg>
                ) : (
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    <polyline points="22,4 12,14.01 9,11.01" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                )}
              </div>
              <div className="result-text">
                <span className="result-label">Classification Result:</span>
                <span className="result-value">{result.toUpperCase()}</span>
              </div>
            </div>
          </div>
        )}

        <div className="footer">
          <p>Built with advanced machine learning algorithms</p>
        </div>
      </div>
    </div>
  );
}

export default App;