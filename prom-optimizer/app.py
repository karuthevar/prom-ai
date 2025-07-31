from flask import Flask, jsonify
import requests
import os
import re

PROMETHEUS_URL = os.environ.get("PROMETHEUS_URL", "http://prometheus:9090")
QUERY_LOG_FILE = os.environ.get("QUERY_LOG_FILE", "/querylog/query.log")

app = Flask(__name__)

@app.route("/metrics-usage")
def metrics_usage():
    try:
        # Get all metric names from Prometheus
        response = requests.get(f"{PROMETHEUS_URL}/api/v1/label/__name__/values")
        response.raise_for_status()
        metrics = response.json().get("data", [])
    except Exception as e:
        return jsonify({"error": f"Failed to fetch metrics from Prometheus: {e}"}), 500

    try:
        with open(QUERY_LOG_FILE, "r") as f:
            query_logs = f.read()
    except Exception as e:
        return jsonify({"error": f"Failed to read query log: {e}"}), 500

    usage_counts = {}
    for metric in metrics:
        count = len(re.findall(rf"\b{re.escape(metric)}\b", query_logs))
        if count > 0:
            usage_counts[metric] = count

    return jsonify(usage_counts)

@app.route("/")
def root():
    return jsonify({
        "message": "Welcome to Prometheus Optimizer App",
        "endpoints": ["/metrics-usage"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
