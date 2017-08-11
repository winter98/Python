'''
CtC 1.8 Zero all elements in the same row or column as a zero in an x by y matrix

Seem to have a lot of index variables but not sure if could do something smarter : no for next etc.

'''
def find_zeros(matrix):
    x = 0
    y = 0
    zeros = []
    while x < dimx:
        while y < dimy:
            if matrix[x][y] == 0:
                zeros.append([x,y])
            y += 1
        x += 1
        y = 0
    return zeros

def zero_rows_columns(matrix, zero_positions):
    for z in zero_positions:
        x = 0
        y = 0
        while x < dimx:
            matrix[x][z[1]] = 0
            x += 1
        while y < dimy:
            matrix[z[0]][y] = 0
            y += 1
    return matrix


def print_matrix(matrix):
    for x in matrix:
        print("\t".join(("%02d" % i) for i in x))

test_matrix = [[1,2,0,4],[2,0,4,5],[4,5,6,7]]
dimx = len(test_matrix)
dimy = len(test_matrix[0])
print_matrix(test_matrix)
print()
print_matrix(zero_rows_columns(test_matrix,find_zeros(test_matrix)))

print("Just for Git")

