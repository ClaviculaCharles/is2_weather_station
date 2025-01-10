import time
import csv

device_path = '/sys/bus/w1/devices/28-03191633aa28/temperature'

def read_temperature():
    """Läser av temperaturen från enheten."""
    with open(device_path, 'r') as file:
        temp_str = file.read().strip()
        temp_c = int(temp_str) / 1000.0
        return temp_c

def main():
    # Definiera parametrar
    duration_seconds = 1
    readings_per_second = 10
    num_measurements = duration_seconds * readings_per_second
    output_file = '/home/rasmus/weather_station/temperature_data.csv'

    # Skapa och öppna CSV-filen
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Measurement Number', 'Temperature (°C)'])  # Header-rad

        # Starta mätningen
        for i in range(num_measurements):
            temp = read_temperature()
            csvwriter.writerow([i + 1, temp])
            print(f"Measurement {i + 1}: Temperature = {temp}°C")
            time.sleep(1 / readings_per_second)

    print(f"Mätdata sparad i {output_file}")

if __name__ == '__main__':
    main()
