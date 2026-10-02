class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_frequency_map = {} #hashmap {b : 1, a: 1, l: 2, o: 2, n: 1}
        balloon_str = "balloon"
        output = 0 

        for char in text: 
            if char in balloon_str:
                if char not in char_frequency_map:
                    char_frequency_map[char] = 1
                else:
                    char_frequency_map[char] += 1
        # if char_frequency_map = {b : 1, a: 1, l: 2, o: 2, n: 1}
        #     return output

        b_count, a_count, l_count, o_count, n_count = 0, 0, 0, 0, 0
        for key, value in char_frequency_map.items():
            if key == 'b':
                b_count = value
            elif key == 'a':
                a_count = value
            elif key == 'l':
                l_count = value
            elif key == 'o':
                o_count = value
            elif key == 'n':
                n_count = value
        
        count = min(b_count, a_count, l_count // 2, o_count // 2, n_count)
        return count