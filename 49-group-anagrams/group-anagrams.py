class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Tuple is hashable, so it can be a dictionary key
            res[tuple(count)].append(s)
        return list(res.values())
