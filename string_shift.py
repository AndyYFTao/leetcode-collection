# https://www.geeksforgeeks.org/string-slicing-python-rotate-string/

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        right_step = 0

        for i in range(len(shift)):
            if shift[i][0] == 0:
                right_step -= shift[i][1]
            else:
                right_step += shift[i][1]

        if right_step == 0:
            return s
        elif right_step > 0:
            return s[len(s) - (right_step % len(s)):] + s[0: len(s) - (right_step % len(s))]
        else:
            return s[-right_step % len(s):] + s[0: -right_step % len(s)]