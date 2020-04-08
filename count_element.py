class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = {}
        for i in arr:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1

        count = 0
        # dictionary sorted by key
        sorted_dict = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
        for j in sorted_dict.keys():
            if (j + 1) in sorted_dict.keys():
                count += sorted_dict[j]

        return count
