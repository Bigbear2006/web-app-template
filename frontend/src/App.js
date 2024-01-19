import { useState, useEffect } from 'react';
import axios from 'axios';
import API from "./api";
import logo from './logo.svg';
import './App.css';

function App() {
  let [msg, setMessage] = useState('')
  let url = `${API.url}message/`

  useEffect(() => {
    axios.post(url)
        .then(rsp => setMessage(rsp.data.message))
  })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a href={url}>{msg}</a>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
