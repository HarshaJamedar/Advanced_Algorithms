
# Problem Statement:

def largest_land_mass(Grid_matrix):

    # Initialize a variable max_land_area to 0. 
    # This variable will keep track of the size of the largest land mass found in the grid.
    max_land_area = 0


    # Iterate over each row in the Grid_matrix using an outer loop.
    # For each row, iterate over each column (element) using an inner loop.
    for row in Grid_matrix:
        for column in row:
            # If the element is 1, then it is not a land mass.
            if column == 1:

                # Set the current element to 0, effectively marking it as visited
                row[column] = 0
                # Count the number of zeros (empty cells) in the current row using row.count(0).
                number_of_zeros=sum(row.count(0) for row in Grid_matrix)

                # If the count is greater than max_land_area, update max_land_area with the new count.
                if number_of_zeros > max_land_area:
                    max_land_area = number_of_zeros

                # Reset the current element back to 1 after calculating the land mass size.
                row[column] = 1

    return max_land_area



Grid_matrix1 = [[0, 1, 1],
               [0, 0, 1],
               [1, 1, 0]]
Grid_matrix2 = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
]
print("The largest Land mass area of grid 1 is:",(largest_land_mass(Grid_matrix1)))
print("The largest Land mass area of grid 2 is:",(largest_land_mass(Grid_matrix2)))
