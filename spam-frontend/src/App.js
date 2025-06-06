import React, {useState} from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';

function App() {
  const [message,setMessage ]= useState('');
  const [result,setResult] = useState('');
  const [loading,setLoading] = useState(false);

  const handlePredict = async()=>{
    setLoading(true);
    try{
      const res = await axios.post('https://localhost:5000/predict',{
        message: message
      });
      setResult(res.data.prediction);
    }catch(err){
      setResult("Error connecting to backend");
    }
  };

  return (
    <div className="App">
      <h2>Spam Classifier</h2>
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <textarea
          placeholder = "Type your message here: "
          value={message}
          onChange = {(e) => setMessage(e.target.value)}

        />
        <br/>
        <button onClick={handlePredict} disabled={loading || !message}>
        {loading ? 'Checking...' : 'Check Message'}
        </button>
              <br />
        {result && (
                <div className={`result ${result}`}>
                  Prediction: <strong>{result.toUpperCase()}</strong>
                </div>
              )}
        </div>
  );
}

export default App;
