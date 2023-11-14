def longestDuration_at_a_station(durations, stations):
    low = max(durations)  # Minimum possible time for a single station
    high = sum(durations)  # Maximum possible time for a single station
    result = high  # Initialize the result with the worst case

    while low <= high:
        mid = (low + high) // 2  # Calculate the midpoint

        station_count = 1  # Initialize the station count to 1
        current_time = 0  # Initialize the current station's time to 0

        for duration in durations:
            # print("This is station count ", station_count, "at duration index:", durations.index(duration))
            # print("This is current time ", current_time," at duration index:", durations.index(duration))
            if current_time + duration > mid:
                station_count += 1
                current_time = duration
            else:
                current_time += duration

        if station_count <= stations:
            # We can optimize further, so update the result
            result = min(result, mid)
            high = mid - 1  # Search in the lower half
        else:
            low = mid + 1  # Search in the upper half

    return result

# Sample input
Durations = [15, 15, 30, 30, 45]
Stations = 3

# Call the function
output = longestDuration_at_a_station(Durations, Stations)
print(output)  # Output: 60

