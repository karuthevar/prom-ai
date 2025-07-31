import React, { useState } from 'react';
import axios from 'axios';

function PromAIApp() {
  const [prometheusUrl, setPrometheusUrl] = useState('');
  const [query, setQuery] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    try {
      const response = await axios.get('http://localhost:8000/analyze', {
        params: {
          prometheus_url: prometheusUrl,
          query: query,
        },
      });
      setResult(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
      setResult(null);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: 'Arial, sans-serif' }}>
      <h2>Prometheus AI Anomaly Detector</h2>
      <div style={{ marginBottom: 10 }}>
        <label>Prometheus URL:</label><br />
        <input
          type="text"
          value={prometheusUrl}
          onChange={(e) => setPrometheusUrl(e.target.value)}
          placeholder="http://localhost:9090"
          style={{ width: '100%' }}
        />
      </div>
      <div style={{ marginBottom: 10 }}>
        <label>PromQL Query:</label><br />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="up"
          style={{ width: '100%' }}
        />
      </div>
      <button onClick={handleAnalyze}>Analyze</button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h4>Result:</h4>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}

      {error && (
        <div style={{ marginTop: 20, color: 'red' }}>
          <h4>Error:</h4>
          <pre>{JSON.stringify(error, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default PromAIApp;