# http://support.ecisolutions.com/doc-ddms/help/reportsmenu/ascii_sort_order_chart.htm

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        star = []
        for i, x in enumerate(s):
            if x == '(':
                stack.append(i)
            elif x == '*':
                star.append(i)
            else:
                if not stack and not star:
                    return False
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
        
        while stack and star:
            if stack.pop() > star.pop():
                return False
        
        if not stack:
            return True
        else:
            return False