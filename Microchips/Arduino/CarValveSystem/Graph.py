import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

# Configure the serial port
serial_port = 'COM3'  # Replace with the appropriate serial port
baud_rate = 9600

# Initialize the data lists
valve_offset_data = []
valve_lift_data = []

# Create the figure and axes for the graph
fig, ax = plt.subplots()

# Define the function to update the graph
def update_graph(frame):
    # Clear the axes
    ax.clear()

    # Plot the valve offset data as a square wave
    ax.step(range(len(valve_offset_data)), valve_offset_data, color='blue', where='post', label='Valve Offset')

    # Plot the valve lift data as a square wave
    ax.step(range(len(valve_lift_data)), valve_lift_data, color='red', where='post', label='Valve Lift')

    # Set the legend
    ax.legend()

    # Set the axis labels
    ax.set_xlabel('Time')
    ax.set_ylabel('Valve Status')

    # Set the title
    ax.set_title('Valve Timing')

    # Set the y-axis limits
    ax.set_ylim(-0.1, 1.1)

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate)

# Define the function to read data from the serial port
def read_serial_data():
    while True:
        try:
            # Read a line of data from the serial port
            line = ser.readline().decode().strip()

            # Skip the line if it contains "Rpm"
            if "Rpm" in line:
                continue

            # Split the line into values
            values = line.split(':')

            # Extract the valve timing values
            rpm = int(values[0])
            valve_offset = float(values[1])
            valve_lift = float(values[2])
            time_between_valve_openings = float(values[3])

            # Calculate the number of samples for each timing value
            samples_per_cycle = 100  # Adjust as needed

            # Generate the valve offset waveform
            valve_offset_waveform = [1] * int(valve_offset * samples_per_cycle) + [0] * int(time_between_valve_openings * samples_per_cycle)

            # Generate the valve lift waveform
            valve_lift_waveform = [1] * int(valve_lift * samples_per_cycle) + [0] * int(time_between_valve_openings * samples_per_cycle)

            # Extend the data lists with the waveform data
            valve_offset_data.extend(valve_offset_waveform)
            valve_lift_data.extend(valve_lift_waveform)

            # Trigger the animation update
            ani.event_source.stop()
            ani.event_source.start()

        except KeyboardInterrupt:
            break

# Start reading data from the serial port in a separate thread
data_thread = threading.Thread(target=read_serial_data)
data_thread.start()

# Create the animation
ani = animation.FuncAnimation(fig, update_graph, interval=100)

# Show the graph
plt.show()

# Close the serial connection
ser.close()
