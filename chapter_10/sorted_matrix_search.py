# python3
# sorted_matrix_search.py - Goes through a sorted M x N matrix and returns the location of a number "num".

def sorted_matrix_search(matrix, num):
    """
    Goes through a sorted M x N matrix and returns the location of a number "num".
    """
    M = len(matrix[0])
    N = len(matrix)

    rows_down = round(num / M)
    cols_over = num % M

    # Check to make sure the first rows down guess isn't larger than the len of N.
    if rows_down > N - 1:
        rows_down = round(N / 2)
    row = matrix[rows_down]

    while row[0] > num or row[-1] < num:
        # if the first element in the row is greater than num
        # Then the whole row is greater, so move up
        if row[0] > num:
            if row == matrix[0]:
                return f"Number {num} is not contained within this matrix."
            rows_down -= 1
            row = matrix[rows_down]
        # if the last element in the row is less than num
        # Then the whole row is less, so move down
        elif row[-1] < num:
            if row == matrix[-1]:
                return f"Number {num} is not contained within this matrix."
            rows_down += 1
            row = matrix[rows_down]
        
    # Check to make sure the first cols_over guess isn't larger than the len of M.    
    if cols_over > M - 1:
        cols_over = round(M / 2)
    guess = row[cols_over]
    last_guess = guess
    while guess != num:
        
        if guess == num:
            break
        elif guess > num:
            # If elem is not contained in the matrix, 
            # This prevents going outside matrix bounds.
            if guess == row[0]:
                return f"Number {num} is not contained within this matrix."
            cols_over -= 1
            guess = row[cols_over]
        elif guess < num:
            # If elem is not contained in the matrix, 
            # This prevents going outside matrix bounds.
            if guess == row[-1]:
                return f"Number {num} is not contained within this matrix."
            cols_over += 1
            guess = row[cols_over]

        if (last_guess > num and guess < num) or (last_guess < num and guess > num):
            return f"Number {num} is not contained within this matrix."    
        last_guess = guess

    print(f"Number {num} is {rows_down} rows down and {cols_over} columns over.")
    total_down = rows_down * M
    return total_down + cols_over


def example():
    M = 10
    N = 15
    sorted_matrix = []
    for y in range(N):
        row = []
        row_indx = y * M
        for x in range(0, M, 2):
            row.append(x + row_indx)
        sorted_matrix.append(row)

    print(sorted_matrix_search(sorted_matrix, 0))
    print(sorted_matrix_search(sorted_matrix, 6))
    print(sorted_matrix_search(sorted_matrix, 10))
    print(sorted_matrix_search(sorted_matrix, 15))
    print(sorted_matrix_search(sorted_matrix, 25))
    print(sorted_matrix_search(sorted_matrix, 135))
    print(sorted_matrix_search(sorted_matrix, 136))
    print(sorted_matrix_search(sorted_matrix, 500))
    print(sorted_matrix_search(sorted_matrix, -12))


if __name__ == "__main__": 
    example()