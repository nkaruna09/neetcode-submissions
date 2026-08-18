class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_sublist = {} # sorted character -> list of anagrams

        for s in strs: 
            k = str(sorted(s))
            if k not in map_sublist: 
                map_sublist[k] = []
            map_sublist[k].append(s)

        return list(map_sublist.values())
        