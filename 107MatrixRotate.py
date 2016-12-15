'''
Rotate matrix : in this case it's 4 x 4 : thinking about how you'd do any regular matrix
90 degree rotation (assuming clockwise) but not implementing here : method should be same - find
distance to centre and reverse

'''
import numpy

def print_matrix(matrix):
    for x in matrix:
        print("\t".join(("%02d" % i) for i in x))

def rotate_matrix(matrix):
    result_matrix = numpy.zeros((4,4))
    xdim = len(matrix)
    ydim = len(matrix[0])
    x = 0
    y = 0
    centre_coord = (xdim - 1) / 2.0
    while x < xdim:
        while y < ydim:
            # works but need to make sure clear on the logic : flipping the x and y for mirror image of walk to centre ...
            result_matrix[centre_coord - (centre_coord - y)][centre_coord + (centre_coord - x)] = matrix[x][y]
            y += 1
        x += 1
        y = 0

    return result_matrix


start_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print_matrix(start_matrix)
print("")
print_matrix(rotate_matrix(start_matrix))