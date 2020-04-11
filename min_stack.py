# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

class Node(object):

    def __init__(self, x):
        self.value = x
        self.next = None


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._top = None
        self.minimum = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self._top is None:
            self._top = Node(x)
            self.minimum = x

        elif x < self.minimum:
            temp = (2 * x) - self.minimum
            new_node = Node(temp)
            new_node.next = self._top
            self._top = new_node
            self.minimum = x

        else:
            new_node = Node(x)
            new_node.next = self._top
            self._top = new_node

        return None

    def pop(self):
        """
        :rtype: None
        """
        if self._top is not None:
            removedNode = self._top.value
            self._top = self._top.next
            if removedNode < self.minimum:
                self.minimum = ((2 * self.minimum) - removedNode)

        return None

    def top(self):
        """
        :rtype: int
        """
        if self._top is not None:
            if self._top.value < self.minimum:
                return self.minimum
            else:
                return self._top.value

    def getMin(self):
        """
        :rtype: int
        """
        if self._top is not None:
            return self.minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()