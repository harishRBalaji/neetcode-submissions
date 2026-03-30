class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> frequencyStringVsListOfStringsMap = new HashMap<>();
        for (String str: strs) {
            int[] frequencyArray = new int[26];
            for (char c: str.toCharArray()) {
                frequencyArray[c - 'a']++;
            }
            String frequencyString = Arrays.toString(frequencyArray);
            frequencyStringVsListOfStringsMap.putIfAbsent(frequencyString, new ArrayList<>());
            frequencyStringVsListOfStringsMap.get(frequencyString).add(str);
        }
        return new ArrayList<>(frequencyStringVsListOfStringsMap.values());
    }
}
