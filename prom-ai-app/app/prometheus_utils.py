from prometheus_api_client import PrometheusConnect
from datetime import datetime, timedelta
import pandas as pd

def get_prometheus_data(prom_url, query, lookback_minutes=1440):
    prom = PrometheusConnect(url=prom_url, disable_ssl=True)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=lookback_minutes)

    metric_data = prom.custom_query_range(
        query=query,
        start_time=start_time,
        end_time=end_time,
        step='1m'
    )

    if not metric_data or not metric_data[0]["values"]:
        return pd.DataFrame()

    values = metric_data[0]["values"]
    df = pd.DataFrame(values, columns=["timestamp", "value"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df["value"] = pd.to_numeric(df["value"])
    return df
