This project is an end-to-end observability solution that uses Prometheus to collect metrics, Python-based AI models to detect anomalies, and a React-based frontend with Grafana for visualization. The AI uses Isolation Forest to identify anomalies in time-series data collected from Prometheus.

🧱 Components
Prometheus: Time-series metric collection

AI Backend (FastAPI + Scikit-learn): Anomaly detection using Isolation Forest

Grafana: Visualize metrics and anomalies

Frontend (React): UI to input Prometheus URL and query and trigger analysis

🚀 Installation Steps
1. Clone the Repository

git clone https://github.com/your-org/ai-observability-stack.git
cd ai-observability-stack
2. Launch the Full Stack with Docker Compose

docker-compose up --build
This will spin up:

Prometheus on http://localhost:9090

FastAPI AI backend on http://localhost:8000

Grafana on http://localhost:3000

React UI on http://localhost:5173 (Vite dev) or via http://localhost if built and served via NGINX

⚙️ Configuration
Prometheus is preconfigured via prometheus.yml

The FastAPI backend supports /analyze?prometheus_url=<>&query=<>

The frontend allows users to provide any Prometheus URL and PromQL query dynamically

📈 Usage
Visit the React frontend at:
http://localhost:5173

Enter:

Prometheus URL (e.g., http://localhost:9090)

PromQL Query (e.g., up, node_cpu_seconds_total)

Click Analyze.

The backend fetches data from Prometheus, runs anomaly detection, and returns a list of outliers.

View the results and explore dashboards via Grafana:
http://localhost:3000

📦 Project Structure

.
├── backend/                 # FastAPI + AI model
├── frontend/                # React UI (Vite)
├── prometheus/              # Prometheus config
├── docker-compose.yml
├── README.md
🧪 Example Query

Prometheus URL: http://localhost:9090
PromQL Query: rate(http_requests_total[5m])
Returns a JSON response with:

Original metric values

Predicted anomaly labels

Timestamps of anomaly events

🛠️ Build Frontend Separately
If you'd like to build and serve the frontend manually:


cd frontend
npm install
npm run dev     # For dev mode
npm run build   # For production build
To serve it with NGINX in Docker:


docker build -t promai-frontend .
docker run -p 80:80 promai-frontend
🧠 Tech Stack
Prometheus

Grafana

Python (FastAPI, Scikit-learn, Pandas)

React + Vite

Docker + Docker Compose

📬 Feedback or Contributions?
Pull requests and issues are welcome!