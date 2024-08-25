import React, { useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const TrendAnalysis = () => {
  const [trendData, setTrendData] = useState(null);
  const [compareData, setCompareData] = useState(null);

  const analyzeTrend = async (e) => {
    e.preventDefault();
    const params = {
      metric: e.target.metric.value,
      time_period: e.target.time_period.value,
    };
    const response = await axios.post('/trend/analyze', params);
    setTrendData(response.data);
  };

  const compareTrends = async (e) => {
    e.preventDefault();
    const params = {
      metric1: e.target.metric1.value,
      metric2: e.target.metric2.value,
      time_period: e.target.time_period.value,
    };
    const response = await axios.post('/trend/compare', params);
    setCompareData(response.data);
  };

  return (
    <div>
      <h2>Trend Analysis</h2>
      <form onSubmit={analyzeTrend}>
        <h3>Analyze Trend</h3>
        <input name="metric" placeholder="Metric" required />
        <input name="time_period" placeholder="Time Period (e.g., M, W, D)" required />
        <button type="submit">Analyze</button>
      </form>
      {trendData && (
        <Line
          data={{
            labels: Object.keys(trendData),
            datasets: [
              {
                label: 'Trend',
                data: Object.values(trendData),
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
              },
            ],
          }}
        />
      )}

      <form onSubmit={compareTrends}>
        <h3>Compare Trends</h3>
        <input name="metric1" placeholder="Metric 1" required />
        <input name="metric2" placeholder="Metric 2" required />
        <input name="time_period" placeholder="Time Period (e.g., M, W, D)" required />
        <button type="submit">Compare</button>
      </form>
      {compareData && <img src={`data:image/png;base64,${compareData.plot}`} alt="Trend Comparison" />}
    </div>
  );
};

export default TrendAnalysis;