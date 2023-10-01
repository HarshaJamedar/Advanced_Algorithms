# The Unique starting City Problem by Harshavardhan , Hyson and Soham Kulkarni
# Emails ID's: harsha_jemedar@csu.fullerton.edu, kulkarni.soham@csu.fullerton.edu, hyson0427@csu.fullerton.edu

# Define a function to find the unique starting city given city_distances, fuel, and mpg.
import matplotlib.pyplot as plt
def unique_starting_city(city_distances, fuel, mpg):
    # Initialize variables to keep track of the current starting city,
    # current fuel, required fuel, and total fuel available.
    start_city = 0
    current_fuel = 0
    required_fuel = 0
    total_fuel = 0

    # Iterate through the list of city distances.
    for i in range(len(city_distances)):
        # Calculate the required fuel to reach the next city based on its distance and MPG.
        required_fuel = city_distances[i] / mpg

        # Add the fuel available at the current city to the total fuel available.
        total_fuel += fuel[i]

        # Update the current fuel by subtracting the required fuel.
        current_fuel += fuel[i] - required_fuel

        # Check if the current fuel becomes negative, indicating that we can't reach the next city.
        if current_fuel < 0:
            # Update the starting city to the next city and reset the current fuel.
            start_city = i + 1
            current_fuel = 0

    # After the loop, check if there is not enough total fuel to complete the trip.
    if total_fuel < 0:
        return -1  # Return -1 to indicate no possible solution.
    else:
        return start_city  # Return the unique starting city.

# Input data
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Check if there is a valid starting city and print the result.
if unique_starting_city(city_distances, fuel, mpg) < 0:
    print("No possible solution")
else:
    print("The unique starting city is:", unique_starting_city(city_distances, fuel, mpg))

    # Sample data points (input sizes and corresponding execution times)
input_sizes = [10, 20, 30, 40, 50]
execution_times = [0.1, 0.4, 0.9, 1.6, 2.5]

    # Plot the data
plt.plot(input_sizes, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('The Island Problem Execution Time')
plt.grid(True)
plt.show()
