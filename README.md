# Maximum Square
This program takes a 2D matrix of 0 and 1's, and determine the
area of the largest square submatrix that contains all 1's.  A square
submatrix is one of equal width and height.

For example, for the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

You can see that the largest square submatrix is
of size 2x2, so max_square.py returns the area which is 4.

`max_square.py` will take its array input from a text file, or+
if an input file is not given, it will take it from stdin.

**Python 3 is required to run this.**
```
usage: python3 max_square.py [-h] [-i [INPUT_FILE]]

Maximum subsquare area calculator

optional arguments:
  -h, --help            Show this help message and exit
  -i [INPUT_FILE]       Input file to process. Will use stdin if ommited
```

On `examples`, you can find several example files to run.
