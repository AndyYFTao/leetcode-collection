# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
# BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [rows, cols] = binaryMatrix.dimensions()
        res = -1
        r = 0
        c = cols - 1
        while (r < rows and c >= 0):
            if binaryMatrix.get(r,c) == 1:
                res = c
                c -= 1
            else:
                r += 1
        return res