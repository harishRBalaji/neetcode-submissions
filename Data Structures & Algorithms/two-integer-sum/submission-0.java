class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        int small = 0, big = 0;
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (hashMap.containsKey(difference)) {
                small = Math.min(hashMap.get(difference), i);
                big = Math.max(hashMap.get(difference), i);
            } else {
                hashMap.put(nums[i], i);
            }
        }
        int[] result = {small, big};
        return result;
    }
}
