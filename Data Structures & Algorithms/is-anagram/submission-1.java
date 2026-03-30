class Solution {
    public boolean isAnagram(String s, String t) {
        int[] counts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            counts[c - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            counts[c - 'a']--;
        }

        for (int count: counts) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
}
