class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_word_list_map = {}

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in anagram_to_word_list_map:
                anagram_to_word_list_map[sorted_word] = []
            anagram_to_word_list_map[sorted_word].append(word)

        result = []
        for value in anagram_to_word_list_map.values():
            result.append(value)
        
        return result