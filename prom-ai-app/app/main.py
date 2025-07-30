from fastapi import FastAPI, Query
from app.prometheus_utils import get_prometheus_data
from app.model import train_and_detect

app = FastAPI()

@app.get("/analyze/")
def analyze(prometheus_url: str = Query(...), query: str = Query(...)):
    df = get_prometheus_data(prometheus_url, query)
    if df.empty:
        return {"error": "No data found"}

    result_df, threshold = train_and_detect(df)
    anomalies = result_df[result_df["anomaly"]]

    return {
        "summary": {
            "total_points": len(df),
            "anomalies_detected": int(anomalies["anomaly"].sum()),
            "threshold": threshold
        },
        "recent_anomalies": anomalies.tail(5).to_dict(orient="records")
    }
