class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> sortedStringVsIndexListMap = new HashMap<>();
        for (String str: strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            sortedStringVsIndexListMap.putIfAbsent(sortedStr, new ArrayList<>());
            sortedStringVsIndexListMap.get(sortedStr).add(str);
        }
        return new ArrayList<>(sortedStringVsIndexListMap.values());
    }
}