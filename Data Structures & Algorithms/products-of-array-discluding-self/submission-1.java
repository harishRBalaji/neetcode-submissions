class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1;
        result[n - 1] = 1;

        int prefixProduct = 1;
        for (int i = 1; i < n; i++) {
            prefixProduct *= nums[i - 1];
            result[i] = prefixProduct;
        }

        int suffixProduct = 1;
        for (int i = n - 2; i >= 0; i--) {
            suffixProduct *= nums[i + 1];
            result[i] *= suffixProduct;
        }
        
        return result;
    }
}  
