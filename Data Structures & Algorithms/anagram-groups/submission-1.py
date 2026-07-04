class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        result=[]
        for s in strs:
            sorted_list=tuple(sorted(s))
            res[sorted_list].append(s)
        for c in res.values():
            result.append(c)
        return result