# https://www.geeksforgeeks.org/string-after-processing-backspace-characters/
# https://github.com/grandyang/leetcode/issues/844

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def reduce(S):
            q = []

            for i in range(0, len(S)):

                if S[i] != '#':
                    q.append(S[i])
                elif len(q) != 0:
                    q.pop()

                    # Build final string
            ans = ""

            while len(q) != 0:
                ans += q[0]
                q.pop(0)
            return ans

        return reduce(S) == reduce(T)