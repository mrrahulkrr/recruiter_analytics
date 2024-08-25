import React from 'react';
import PredictiveAnalytics from './components/PredictiveAnalytics';
import TrendAnalysis from './components/TrendAnalysis';

function App() {
  return (
    <div className="App">
      <h1>Recruitment Analytics</h1>
      <PredictiveAnalytics />
      <TrendAnalysis />
    </div>
  );
}

export default App;