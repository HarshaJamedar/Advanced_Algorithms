


def largest_land_mass(Grid_matrix):
    max_land_area = 0
    
    for row in Grid_matrix:

        for column in row:
            # print("this is the row",row)
            # print("this is the column",column)
            if column == 1:
                row[column] = 0
                # print("the changed row",row)
                # print("the updated matrix",Grid_matrix)
                number_of_zeros=sum(row.count(0) for row in Grid_matrix)
                if number_of_zeros > max_land_area:
                    max_land_area = number_of_zeros
                row[column] = 1


    return max_land_area









Grid_matrix = [[0, 1, 1],
               [0, 0, 1],
               [1, 1, 0]]
# print("number of zeros",sum(row.count(0) for row in Grid_matrix))

print("The largest Land mass area is:",(largest_land_mass(Grid_matrix)))