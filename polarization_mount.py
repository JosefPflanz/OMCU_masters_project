import serial
import time

# Replace with your actual COM port
com_port = 'COM3'
baud_rate = 9600  # Default for Elliptec

# Connect to the controller
ser = serial.Serial(com_port, baud_rate, timeout=1)

# Pause to allow device to initialize
time.sleep(2)

# Define a simple function to send commands
def send_command(command: bytes):
    ser.write(command)
    time.sleep(0.1)
    response = ser.read_all()
    print(f"Response: {response}")

def go_home():
    send_command(b'\x01ho')

def turn_fw():
    send_command(b'\x01fw')

def turn_bw():
    send_command(b'\x01bw')


# Close port after use
ser.close()

