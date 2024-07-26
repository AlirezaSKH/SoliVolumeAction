import pandas as pd

def detect_volume_zones(data):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Rename columns for better readability
    df.columns = ['close', 'high', 'low', 'open', 'status', 'timestamp', 'volume']
    
    # Convert timestamps to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    # Example threshold logic: high volume zones
    volume_threshold = df['volume'].mean() + df['volume'].std()  # Example threshold
    volume_zones = df[df['volume'] > volume_threshold]
    
    return volume_zones
