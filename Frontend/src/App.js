
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [info, setInfo] = useState(null);

  useEffect(() => {
    const fetchData = async() => {
      try{
        const response = await fetch('http://localhost:8000'); //port where the backend comes from
        const data = await response.json();
        // sets the parsed json info from req to the info constant decalred aboce
        setInfo(data);
      
    } catch (error){
      console.error('Cannot get data: ', error);
    }


  }
  fetchData();
}, []); //array for second argument
    

  return (
    <div>
      {info ? (
      <pre>
        <code>{JSON.stringify(info, null, 2)}</code>
      </pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
