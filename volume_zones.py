import pandas as pd

def calculate_swing_points(data):
    # Convert data to DataFrame and rename columns
    df = pd.DataFrame(data)
    df.columns = ['close', 'high', 'low', 'open', 'status', 'timestamp', 'volume']
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Identify major swings
    df['swing'] = ((df['close'] - df['close'].shift()) * (df['close'] - df['close'].shift(-1)) < 0).astype(int)
    swings = df[df['swing'] == 1]

    # Select the last two swings
    recent_swings = swings.tail(2)  # Get the last two swings

    # Print detected swings for debugging
    print("Detected Swings:")
    print(recent_swings)

    return recent_swings
