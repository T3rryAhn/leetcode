class Solution {
    public int removeDuplicates(int[] nums) {
        int pre = nums[0];
        int k = 0;

        for (int i = 1; i < nums.length; i++) {
            if (pre != nums[i]) {
                k++;
                pre = nums[i];
                nums[k] = nums[i];
            }
        }
        return k + 1;
    }
}