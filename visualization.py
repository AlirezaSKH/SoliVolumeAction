import pandas as pd
import plotly.graph_objects as go
from datetime import timedelta

def plot_swings(swings, data):
    # Convert data to DataFrame and rename columns
    df = pd.DataFrame(data)
    df.columns = ['close', 'high', 'low', 'open', 'status', 'timestamp', 'volume']
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Calculate padding time
    padding_time = timedelta(days=10)  # Add 10 days of padding, adjust as needed

    # Plot the candlestick chart
    fig = go.Figure(data=[
        go.Candlestick(x=df['timestamp'],
                       open=df['open'],
                       high=df['high'],
                       low=df['low'],
                       close=df['close'])
    ])

    # Add arrows for swings
    for index, row in swings.iterrows():
        fig.add_annotation(
            x=row['timestamp'], y=row['high'] if row['swing'] else row['low'],
            ax=row['timestamp'], ay=row['high'] + (df['high'].max() - df['low'].min()) * 0.1 if row['swing'] else row['low'] - (df['high'].max() - df['low'].min()) * 0.1,
            xref="x", yref="y",
            showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='blue',
            text="Swing"
        )

    # Update x-axis to include padding
    fig.update_xaxes(range=[df['timestamp'].min(), df['timestamp'].max() + padding_time])

    fig.show()
