class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefixProductArray = new int[n];
        int[] suffixProductArray = new int[n];
        int prefixProduct = 1;
        int suffixProduct = 1;
        prefixProductArray[0] = 1;
        suffixProductArray[n - 1] = 1;
        for (int i = 1; i < n; i++) {
            prefixProductArray[i] = prefixProductArray[i - 1] * nums[i - 1];
        }

        for (int i = n - 2; i >= 0; i--) {
            suffixProductArray[i] = suffixProductArray[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < n; i++) {
            suffixProductArray[i] *= prefixProductArray[i];
        }
        return suffixProductArray;
    }
}  
