# https://www.geeksforgeeks.org/print-anagrams-together-python-using-list-dictionary/?ref=rp

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()