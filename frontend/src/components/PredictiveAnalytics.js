import React, { useState } from 'react';
import axios from 'axios';

const PredictiveAnalytics = () => {
  const [timeToHire, setTimeToHire] = useState(null);
  const [candidateSuccess, setCandidateSuccess] = useState(null);

  const predictTimeToHire = async (e) => {
    e.preventDefault();
    const features = {
      role_type: e.target.role_type.value,
      location: e.target.location.value,
      experience: parseInt(e.target.experience.value),
    };
    const response = await axios.post('/predict/time_to_hire', features);
    setTimeToHire(response.data.prediction);
  };

  const predictCandidateSuccess = async (e) => {
    e.preventDefault();
    const features = {
      education: e.target.education.value,
      experience: parseInt(e.target.experience.value),
      time_to_hire: parseInt(e.target.time_to_hire.value),
    };
    const response = await axios.post('/predict/candidate_success', features);
    setCandidateSuccess(response.data.prediction);
  };

  return (
    <div>
      <h2>Predictive Analytics</h2>
      <form onSubmit={predictTimeToHire}>
        <h3>Predict Time to Hire</h3>
        <input name="role_type" placeholder="Role Type" required />
        <input name="location" placeholder="Location" required />
        <input name="experience" type="number" placeholder="Experience (years)" required />
        <button type="submit">Predict</button>
      </form>
      {timeToHire !== null && <p>Predicted Time to Hire: {timeToHire} days</p>}

      <form onSubmit={predictCandidateSuccess}>
        <h3>Predict Candidate Success</h3>
        <input name="education" placeholder="Education" required />
        <input name="experience" type="number" placeholder="Experience (years)" required />
        <input name="time_to_hire" type="number" placeholder="Time to Hire (days)" required />
        <button type="submit">Predict</button>
      </form>
      {candidateSuccess !== null && <p>Predicted Candidate Success: {(candidateSuccess * 100).toFixed(2)}%</p>}
    </div>
  );
};

export default PredictiveAnalytics;