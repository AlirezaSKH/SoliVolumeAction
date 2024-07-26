import pandas as pd
import plotly.graph_objects as go

def plot_volume_zones(volume_zones, data):
    # Convert data to DataFrame and rename columns
    df = pd.DataFrame(data)
    df.columns = ['close', 'high', 'low', 'open', 'status', 'timestamp', 'volume']
    
    # Convert timestamps to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    volume_zones['timestamp'] = pd.to_datetime(volume_zones['timestamp'], unit='s')
    
    # Plot the candlestick chart with volume zones
    fig = go.Figure(data=[
        go.Candlestick(x=df['timestamp'],
                       open=df['open'],
                       high=df['high'],
                       low=df['low'],
                       close=df['close']),
        go.Scatter(x=volume_zones['timestamp'], y=volume_zones['close'], mode='markers', name='Volume Zones', marker=dict(color='red', size=10))
    ])
    fig.show()
