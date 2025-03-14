import logo from './logo.svg';
import './App.css';

//Default
/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
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
}*/


//Example-1
/*
import Example1 from './Example1.js';
function App() {
  return(
  <div>
    <h1>useEffect() Example</h1>
    <hr />
    <Example1 />
  </div>
  );
}
*/

//Example-2

import React, { useState } from 'react';

function App() {
  const [email, setEmail] = useState(null);
  const [cellphone, setCellphone] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  async function fetchData() {
    try {
      // Set loading to true while data is being fetched
      setIsLoading(true);
      
      // Fetch data from an API
      const response = await fetch('https://api.randomuser.me/?nat=US&results=1');
      if (response.ok) {
        // Check if the request was successful
        let { results } = await response.json();
        // Parse the JSON data from the response
        let { email, cell } = results[0];
        // Set the fetched data to the state
        setEmail(email);
        setCellphone(cell);
      } 
      else {
        // Handle error if the request was not successful
        console.error('Failed to fetch data:', response.statusText);
      }
    } 
    catch (error) {
      // Handle network errors or other exceptions
      console.error('Error during data fetching:', error);
    } 
    finally {
      setIsLoading(false); // Set loading to false once data fetching is complete
    }
  }

  return (
    <div>
      <h1>Fetch Data Without useEffect</h1>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <button onClick={fetchData}>Fetch Data</button>
          {email && (
            <div>
              <h2>Fetched Data:</h2>
              <pre>{email}</pre>
              <pre>{cellphone}</pre>
            </div>
            )
          }
        </div>
      )
      }
    </div>
  );
}


//Example-3
/*
import React, { useState } from 'react';

function App() {
  const [email, setEmail] = useState(null);
  const [cellphone, setCellphone] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  function fetchData() {
    // Set loading to true while data is being fetched
    setIsLoading(true);
    
    // Fetch data from an API using .then()
    fetch('https://api.randomuser.me/?nat=US&results=1')
    .then((response) => response.json())
    .then((data) => {
      // Parse the JSON data from the response
      let { email, cell } = data.results[0];
      
      // Set the fetched data to the state
      setEmail(email);
      setCellphone(cell);
    })
    .catch((error) => {
      // Handle error if the request was not successful
      console.error('Failed to fetch data:', error.message);
    })
    .finally(() => {
      // Set loading to false once data fetching is complete
      setIsLoading(false);
    }); 
  }


  return (
    <div>
      <h1>Fetch Data Without useEffect</h1>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <button onClick={fetchData}>Fetch Data</button>
          {email && (
            <div>
              <h2>Fetched Data:</h2>
              <pre>{email}</pre>
              <pre>{cellphone}</pre>
            </div>
            )
          }
        </div>
      )
      }
    </div>
  );
}
*/

//Example-4
/*
import React, { useState, useEffect } from 'react';

function App() {
  const [email, setEmail] = useState(null);
  const [cellphone, setCellphone] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  function fetchData() {
    // Set loading to true while data is being fetched
    setIsLoading(true);
    
    // Fetch data from an API using .then()
    fetch('https://api.randomuser.me/?nat=US&results=1')
    .then((response) => response.json())
    .then((data) => {
      // Parse the JSON data from the response
      let { email, cell } = data.results[0];
      
      // Set the fetched data to the state
      setEmail(email);
      setCellphone(cell);
    })
    .catch((error) => {
      // Handle error if the request was not successful
      console.error('Failed to fetch data:', error.message);
    })
    .finally(() => {
      // Set loading to false once data fetching is complete
      setIsLoading(false);
    }); 
  }

  useEffect(() => {
    fetchData();
  },[]);  

  return (
    <div>
      <h1>Fetch Data With useEffect</h1>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <button onClick={fetchData}>Fetch Data</button>
          {email && (
            <div>
              <h2>Fetched Data:</h2>
              <pre>{email}</pre>
              <pre>{cellphone}</pre>
            </div>
            )
          }
        </div>
      )
      }
    </div>
  );
}
*/

//Example-5
/*
import React, { useState, useEffect } from 'react';

function App() {
  // State to store the fetched data
  const [data, setData] = useState(null);
  // State to track loading status
  const [isLoading, setIsLoading] = useState(true);
  
  // Effect to fetch data when the component mounts
  useEffect(() => {
    // Fetch data from an API
    fetch('https://api.randomuser.me/?nat=US&results=1')
    .then((response) => response.json())
    .then((data) => {
      // Set the fetched data to the state
      setData(data.results[0]);
      // Set loading to false once data fetching is complete
      setIsLoading(false);
    })
    .catch((error) => {
      // Handle errors
      console.error('Error fetching data:', error);
      // Set loading to false in case of an error
      setIsLoading(false); 
    }); 
  }, []);

  return (
    <div>
      <h1>Simple Example with useEffect and Fetch</h1>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <h2>Fetched Data:</h2>
          <pre>{data.email}</pre>
          <pre>{data.cell}</pre>
          <pre>{data.phone}</pre>
        </div>
        )
      }
    </div>
  );
}
*/

export default App;
