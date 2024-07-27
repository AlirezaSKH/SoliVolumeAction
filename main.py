from data_collection import get_forex_data
from volume_zones import calculate_swing_points
from visualization import plot_swings

# Define test parameters
symbol = 'OANDA:EUR_USD'  # Example forex symbol
resolution = '60'  # Hourly data
from_time = 1721908249  # New start timestamp
to_time = 1722011512  # New end timestamp

# Fetch data
data = get_forex_data(symbol, resolution, from_time, to_time)

# Detect swing points
swings = calculate_swing_points(data)

# Plot swings
plot_swings(swings, data)

# Print detected swings (for debugging purposes)
print(swings)
