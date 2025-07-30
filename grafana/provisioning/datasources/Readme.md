# AI-Driven Observability Stack with Prometheus and Grafana

This project demonstrates an end-to-end AI-powered observability platform built using Docker Compose. It includes:

- **Prometheus** for metrics collection
- **Node Exporter** to gather system-level metrics
- **Blackbox Exporter** to monitor external HTTP endpoints (e.g., social media latency)
- **Grafana** for visualization
- **AI Metrics Analyzer**: a FastAPI app using an Autoencoder neural network (TensorFlow/Keras) to detect anomalies in Prometheus metrics

---

## 🚀 Features

- Scrapes and stores system metrics using Prometheus
- Probes uptime and latency of top 10 social media websites using Blackbox Exporter
- Visualizes metrics via Grafana dashboards
- Detects anomalies in any Prometheus metric using an AI Autoencoder model
- Simple REST API to trigger AI-based analysis

---

## 📦 Stack Components

| Service         | Description                           | Port |
|----------------|---------------------------------------|------|
| Prometheus      | Time-series DB and scraper            | 9090 |
| Node Exporter   | Collects host-level metrics           | 9100 |
| Blackbox Exporter | Monitors HTTP endpoints            | 9115 |
| AI Analyzer App | Detects anomalies in metrics (FastAPI + TensorFlow) | 8080 |
| Grafana         | Dashboards and visualization          | 3000 |

---

## 🧠 AI Analyzer: How It Works

- Pulls historical time-series data from Prometheus using HTTP API
- Normalizes the data and trains an **Autoencoder neural net**
- Calculates reconstruction error to flag anomalies
- Returns JSON with:
  - Summary stats
  - Anomaly count
  - Recent anomalous points

---

## 📂 Project Structure

```text
demo-stack/
├── docker-compose.yml
├── prometheus/
│   └── prometheus.yml
├── blackbox/
│   └── blackbox.yml
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── datasource.yml
├── ai-metrics-app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── model.py
│       └── prometheus_utils.py


How to Use
1. Clone and Build
bash
Copy
Edit
git clone https://github.com/your-org/ai-prometheus-stack.git
cd ai-prometheus-stack
docker compose up --build
2. Access the Services
Grafana: http://localhost:3000 (admin / admin)

Prometheus: http://localhost:9090

AI API: http://localhost:8080/analyze

3. Example AI Query
To analyze anomalies in Prometheus's own availability:

bash
Copy
Edit
curl "http://localhost:8080/analyze?prometheus_url=http://prometheus:9090&query=up"
📊 Grafana Configuration
Grafana is automatically preconfigured with:

Prometheus as the default data source

Create new dashboards to visualize:

Node Exporter system metrics

Blackbox probe latency

(Optional) Custom annotations from the AI app

🔮 Future Enhancements
Push anomaly results back to Prometheus

Add alerting based on anomaly counts

Integrate LSTM or Prophet for predictive forecasting

Host the AI app as a microservice (e.g., ECS or Azure App Service)

🧪 Social Media Sites Monitored
Via Blackbox Exporter:

Twitter

Facebook

Instagram

LinkedIn

YouTube

Pinterest

TikTok

Reddit

Snapchat

Threads

📄 License
MIT License

🙋‍♀️ Questions?
Raise an issue or contact the maintainer at your.email@domain.com.