class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if stones == []:
            return 0

        while len(stones) > 1:
            sorted_stones = sorted(stones, reverse=True)
            duo = sorted_stones[0:2]
            if (duo[0] != duo[1]):
                sorted_stones.append(abs(duo[0] - duo[1]))
            elif len(sorted_stones) == 2:
                return 0
            stones = sorted_stones[2:]

        return stones[0] if len(stones) == 1 else 0
