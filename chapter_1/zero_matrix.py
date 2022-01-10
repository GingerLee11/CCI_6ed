# python3
# zero_matrix.py - For a matrix with M x N rows and columns, if one of the elements is 0, 
# then the entire row and column containing that 0 is also 0.

def zero_matrix(matrix):
    # Create row and column lists to store the locations of the zeros
    row_list = set()
    column_list = set()

    # Search through the matrix for zeros and then stores their locations
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][column] == 0:
                row_list.add(row)
                column_list.add(column)

    # Set all the elements in the rows and columns containing the zeros to zero        
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][column] == 0:
                continue
            elif row in row_list:
                matrix[row][column] = 0
            elif column in column_list:
                matrix[row][column] = 0
    
    return matrix


matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [1, 2, 0, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 0, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 0, 5, 6, 7, 8, 9, 10],
]


zero_matrix(matrix)

