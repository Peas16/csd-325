#Paul Fralix, 06/15/2025, Assignment 4.2
# Sitka Weather Viewer
# This program reads weather data from a CSV file and allows users to view high and low temperatures for Sitka, Alaska in 2018.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Read data once and store highs/lows
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Main menu loop
def main():
    print("Welcome to Sitka Weather Viewer")
    while True:
        print("\nMenu:")
        print("1. Highs - View high temperatures")
        print("2. Lows - View low temperatures")
        print("3. Exit - Quit the program")

        choice = input("Please select an option (Highs/Lows/Exit): ").strip().lower()

        if choice == 'highs':
            plot_temperatures(dates, highs, 'red', 'Daily High Temperatures - 2018')
        elif choice == 'lows':
            plot_temperatures(dates, lows, 'blue', 'Daily Low Temperatures - 2018')
        elif choice == 'exit':
            print("Thanks for using the Sitka Weather Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please type 'Highs', 'Lows', or 'Exit'.")

# Plot function
def plot_temperatures(dates, temps, color, title):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Run the program
if __name__ == "__main__":
    main()

