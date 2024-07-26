import plotly.graph_objects as go

def plot_volume_zones(volume_zones):
    fig = go.Figure(data=[
        go.Candlestick(x=volume_zones['time'],
                       open=volume_zones['open'],
                       high=volume_zones['high'],
                       low=volume_zones['low'],
                       close=volume_zones['close'])
    ])
    fig.show()
