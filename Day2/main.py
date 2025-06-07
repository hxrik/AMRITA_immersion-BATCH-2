import network
import time
from machine import Pin


# --- Sensor Setup ---

pir_sensor = Pin(15, Pin.IN)  # PIR sensor
ir_sensor = Pin(14, Pin.IN, Pin.PULL_DOWN)  # IR sensor (button)

# Color sensor simulated with buttons
red_btn = Pin(13, Pin.IN, Pin.PULL_DOWN)
green_btn = Pin(12, Pin.IN, Pin.PULL_DOWN)
blue_btn = Pin(11, Pin.IN, Pin.PULL_DOWN)

# --- Functions ---

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting to Wi-Fi...", end='')
    while not wlan.isconnected():
        print('.', end='')
        time.sleep(0.5)
    print("\n✅ Connected! IP:", wlan.ifconfig()[0])

def detect_color():
    if red_btn.value():
        return 1  # Red
    elif green_btn.value():
        return 2  # Green
    elif blue_btn.value():
        return 3  # Blue
    else:
        return 0  # No color selected

# --- Main Program ---

def main():
    # Optional Wi-Fi connection — remove if not needed
    # connect_wifi()

    print("📡 Monitoring started...")

    while True:
        pir_state = pir_sensor.value()
        ir_state = ir_sensor.value()
        color_code = detect_color()

        print(f"📟 PIR: {pir_state}, IR: {ir_state}, Color: {color_code}")

        time.sleep(2)  # Faster refresh rate now since no ThingSpeak delay

if __name__ == '__main__':
    main()
