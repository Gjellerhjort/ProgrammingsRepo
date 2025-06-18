import serial
import matplotlib.pyplot as plt
import math

# Function to parse the serial data and extract valve information
def parse_serial_data(serial_data):
    data_lines = serial_data.strip().split('\n')
    if len(data_lines) < 4:
        print("Incomplete serial data")
        return None
    
    try:
        rpm = int(data_lines[0].split(': ')[1])
        valve_offset_time = float(data_lines[1].split(': ')[1])
        valve_lift_time = float(data_lines[2].split(': ')[1])
        time_between_valve_openings = float(data_lines[3].split(': ')[1])
        return rpm, valve_offset_time, valve_lift_time, time_between_valve_openings
    except (IndexError, ValueError):
        print("Invalid serial data format")
        return None

# Function to update the valve diagram
def update_valve_diagram(rpm, valve_offset_time, valve_lift_time, time_between_valve_openings):
    # Check if time_between_valve_openings is valid
    if time_between_valve_openings == 0 or math.isnan(time_between_valve_openings):
        print("Invalid time_between_valve_openings value")
        return
    
    # Calculate the valve open and close times in seconds
    valve_open_times = []
    valve_close_times = []
    current_time = 0
    while current_time <= valve_lift_time:
        valve_open_times.append(current_time)
        valve_close_times.append(current_time + valve_offset_time)
        current_time += time_between_valve_openings
    
    if not valve_open_times or not valve_close_times:
        print("No valve opening/closing times calculated")
        return
    
    # Clear the current plot
    plt.clf()
    
    # Plot the valve opening and closing lines
    plt.plot(valve_open_times, [valve_lift_time] * len(valve_open_times), 'r', label='Valve 1')
    plt.plot(valve_close_times, [valve_lift_time] * len(valve_close_times), 'r')
    
    # Set the x-axis limits based on the duration of a single valve opening
    plt.xlim(0, valve_lift_time)
    
    # Set the y-axis limits based on the valve lift time
    plt.ylim(-0.1, valve_lift_time + 0.1)
    
    # Set the y-axis ticks and labels
    plt.yticks([0, valve_lift_time], ['Valve 1', ''])
    plt.ylabel('Valve Lift')
    
    # Set the x-axis ticks and labels
    plt.xticks([valve_offset_time, valve_lift_time], ['Offset', 'Lift Time'])
    plt.xlabel('Time (s)')
    
    # Set the title of the plot
    plt.title(f'Valve Diagram (RPM: {rpm})')
    
    # Show the legend
    plt.legend()
    
    # Draw the updated plot
    plt.draw()
    plt.pause(0.001)

# Serial port configuration
serial_port = 'COM3'  # Replace with the appropriate port for your system
baud_rate = 9600

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)

# Create the initial plot
plt.figure(figsize=(10, 6))

# Read serial data and update the valve diagram
while True:
    # Read each line of serial data
    rpm_line = ser.readline().decode(encoding='utf-8', errors='ignore').strip()
    offset_line = ser.readline().decode().strip()
    lift_line = ser.readline().decode().strip()
    time_line = ser.readline().decode().strip()
    
    # Combine the lines into a single serial data string
    serial_data = f"{rpm_line}\n{offset_line}\n{lift_line}\n{time_line}"
    
    # Parse the serial data
    data = parse_serial_data(serial_data)
    
    if data:
        rpm, valve_offset_time, valve_lift_time, time_between_valve_openings = data
        # Update the valve diagram
        update_valve_diagram(rpm, valve_offset_time, valve_lift_time, time_between_valve_openings)
