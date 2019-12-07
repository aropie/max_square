#!/usr/bin/env python3
"""
Have the function maximum_square(array) take the array parameter
being passed which will be a 2D matrix of 0 and 1's, and determine the
area of the largest square submatrix that contains all 1's.  A square
submatrix is one of equal width and height, and your program should
return the area of the largest submatrix that contains only 1's. For
example: if array is ["10100", "10111", "11111", "10010"] then this
looks like the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

For the input above, you can see that the largest square submatrix is
of size 2x2, so your program should return the area which is 4.  You
can assume the input will not be empty.
"""
import argparse
import sys


def maximum_square(array):
    """Returns the area of the maxmium subsquare that contains only '1's.

    The idea behind the algorithm is to have an auxiliary array
    where each cell represent the maximum square achievable with
    its rightmost bottom corner on said cell. That said, each cell
    on the auxiliary matrix can only be as big as its surrounding
    cells, plus one. That's why this algorithm runs on O(m*n) time
    with an array of m*n.
    """
    if not array or not array[0]:
        return 0
    height = len(array)
    width = len(array[0])
    aux_array = [['0' for x in range(width)] for y in range(height)]

    # Copy the first row and first column of array into the aux_array.
    try:
        aux_array[0] = [int(elem) for elem in array[0]]
        for idx, row in enumerate(aux_array):
            row[0] = int(array[idx][0])
    except ValueError as e:
        raise ValueError('array is not a binary matrix') from e

    maximum_square_found = 1 if '1' in array[0] else 0
    for i in range(1, height):
        for j in range(1, width):
            try:
                current_cell = array[i][j]
            except IndexError:
                raise ValueError('array is not a valid matrix')
            # If cell is 0, there's no square possible using the current cell.
            if current_cell == '0':
                aux_array[i][j] = 0
            elif current_cell == '1':
                # The minimum of the surrounding cells is the maximum that can
                # grow the square, and to that we add 1 to account for the
                # current cell
                maximum_square_at_ij = min(aux_array[i-1][j],
                                           aux_array[i-1][j-1],
                                           aux_array[i][j-1]) + 1
                aux_array[i][j] = maximum_square_at_ij
                maximum_square_found = max(maximum_square_at_ij,
                                           maximum_square_found)
            else:
                raise ValueError('array is not a binary matrix')
    return maximum_square_found ** 2


def prettify_array(array):
    """Transforms an array into a printable string."""
    return '\n'.join(array)


def main():
    parser = argparse.ArgumentParser('Maximum subsquare area calculator')
    parser.add_argument('-i', '--input-file', nargs='?',
                        help=('Input file to process. '
                              'Will use stdin if ommited'),
                        type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()

    array = args.input_file.read().splitlines()
    area = maximum_square(array)
    print('\nFor array:\n{}'.format(prettify_array(array)))
    print('The area of the maximum subsquare is {}'.format(area))


if __name__ == '__main__':
    main()
