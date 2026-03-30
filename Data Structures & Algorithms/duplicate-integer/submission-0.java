class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hashMap = new HashSet<>();
        for (int num: nums) {
            if (hashMap.contains(num)) {
                return true;
            } else {
                hashMap.add(num);
            }
        }
        return false;
    }
}