class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        source_to_dest_map = {}
        dest_to_source_map = {}
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in source_to_dest_map and source_to_dest_map[c1] != c2) or (c2 in dest_to_source_map and dest_to_source_map[c2] != c1):
                return False
            source_to_dest_map[c1] = c2
            dest_to_source_map[c2] = c1
        
        return True