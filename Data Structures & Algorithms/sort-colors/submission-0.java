class Solution {
    public void sortColors(int[] nums) {
        int redCount = 0;
        int whiteCount = 0;
        int blueCount = 0;

        for (int num: nums) {
            if (num == 0) {
                redCount++;
            } else if (num == 1) {
                whiteCount++;
            } else if (num == 2) {
                blueCount++;
            }
        }
 
        int i = 0;
        while (i < nums.length && redCount > 0) {
            nums[i] = 0;
            redCount--;
            i++;
        }

        while (i < nums.length && whiteCount > 0) {
            nums[i] = 1;
            whiteCount--;
            i++;
        }

        while (i < nums.length && blueCount > 0) {
            nums[i] = 2;
            blueCount--;
            i++;
        }
    }
}