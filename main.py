from data_collection import get_forex_data
from volume_zones import detect_volume_zones
from visualization import plot_volume_zones

# Define test parameters
symbol = 'OANDA:EUR_USD'  # Example forex symbol
resolution = 'D'  # Daily data
from_time = 1700188249  # Example start timestamp
to_time = 1722011512  # Example end timestamp

# Fetch data
data = get_forex_data(symbol, resolution, from_time, to_time)

# Detect volume zones
volume_zones = detect_volume_zones(data)

# Plot volume zones
plot_volume_zones(volume_zones, data)

# Print detected volume zones (for debugging purposes)
print(volume_zones)
