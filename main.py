from data_collection import get_forex_data
from volume_zones import detect_volume_zones
from alert_system import send_email_alert
from visualization import plot_volume_zones

# Example usage
data = get_forex_data('OANDA:EUR_USD', 'D', 1590988249, 1591852249)
volume_zones = detect_volume_zones(data)
plot_volume_zones(volume_zones)

# Check for specific condition to send an alert
if not volume_zones.empty:
    send_email_alert('Volume Alert', 'High volume detected at ...', 'user@example.com')
