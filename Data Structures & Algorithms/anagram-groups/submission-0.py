class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sSorted = ''.join(sorted(s))
            res[sSorted].append(s)

        return list(res.values())