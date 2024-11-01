import math

# Define the bus stops and distances
bus_stops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]
path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
n = len(bus_stops)

# Input source and destination
source = input("Enter the Source Bus Stop (2-letter code): ").strip().upper()
destination = input("Enter the Destination Bus Stop (2-letter code): ").strip().upper()

# Check for valid bus stops
if source not in bus_stops or destination not in bus_stops:
    print("INVALID OUTPUT")
else:
    # Find the indices of the source and destination
    source_index = bus_stops.index(source)
    destination_index = bus_stops.index(destination)

    # Calculate the distance
    if destination_index >= source_index:
        distance = sum(path[source_index:destination_index])  # Sum distances in between
    else:
        distance = sum(path[source_index:]) + sum(path[:destination_index])  # Wrap around

    # Calculate fare
    fare = math.ceil(distance / 1000 * 5)  # Calculate and ceil fare

    # Print the result
    print(f"{fare}.0 INR")

