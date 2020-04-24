# https://www.geeksforgeeks.org/bitwise-and-or-of-a-range/

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # Find position of MSB in n. For example
        # if n = 17, then position of MSB is 4.
        # If n = 7, value of MSB is 3
        def msbPos(n):

            msb_p = -1
            while (n > 0):
                n = n >> 1
                msb_p += 1

            return msb_p

        res = 0
        while (m > 0 and n > 0):
            msb_p1 = msbPos(m)
            msb_p2 = msbPos(n)

            # If positions are not same, return
            if (msb_p1 != msb_p2):
                break

            # Add 2^msb_p1 to result
            msb_val = (1 << msb_p1)
            res = res + msb_val

            # subtract 2^msb_p1 from x and y.
            m = m - msb_val
            n = n - msb_val

        return res