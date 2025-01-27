public class Solution {
    public int Search(int[] nums, int target) {
        int low = 0;
        int high = nums.Length - 1;

        while (low <= high) {
            int med = (low + high) / 2;

            if (nums[med] == target) {
                return med;
            } else if (target < nums[med]) {
                high = med - 1;
            } else { // target > nums[med]
                low = med + 1;
            }
        }

        return -1;
    }
}
