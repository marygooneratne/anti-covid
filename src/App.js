import React from 'react';
import logo from './logo.svg';
import './App.css';
import duke from './assets/duke_logo.png'


function App() {
  const cardHeight = 0.63 * window.innerHeight
  return (
    <div className="App" style={{ backgroundColor: "#111D2F", position: 'absolute', height: '100%', width: '100%' }}>
      <div style={{ display: "flex", flexDirection: "column" }}>
        <div style={{ height: '20%' }}>
          <p style={{ textShadow: "-10px 10px 10px #000000", color: 'white', fontSize: 80, fontWeight: 'bold', marginTop: 10, marginBottom: 0 }}>COVID-19 DATA ROOM</p>
          <p style={{ color: 'white', fontSize: 20, marginBottom: 20, marginTop: 0 }}>PRESENTED BY DUKE UNIVERSITY APPLIED MACHINE LEARNING GROUP</p>
        </div>
        <div style={{ display: "flex", flexDirection: "row", marginBottom: -60, justifyContent: 'space-around', zIndex: 10 }}>
          <p style={{ textShadow: "-5px 5px 5px #000000", color: 'white', fontSize: 50, marginTop: 10, marginBottom: 0 }}>Economy</p>
          <p style={{ textShadow: "-5px 5px 5px #000000", color: 'white', fontSize: 50, marginTop: 10, marginBottom: 0 }}>Health System</p>

        </div>
        <div style={{ display: "flex", flexDirection: "row", height: "80%", justifyContent: 'space-around' }}>
          <div style={{ borderRadius: 10, backgroundColor: "rgba(100,100,100,0.3)", width: '45%', height: cardHeight, margin: 30 }} />
          <div style={{ borderRadius: 10, backgroundColor: "rgba(100,100,100,0.3)", width: '45%', height: cardHeight, margin: 30 }} />
        </div>
        <img src={duke} style={{ width: '10%', height: '10%', alignSelf: 'center' }} />
      </div>
5    </div>
  );
}

export default App;
