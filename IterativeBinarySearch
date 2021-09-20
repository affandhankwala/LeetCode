class Solution {
    public int search(int[] nums, int target) {
        //Do it iteratively
        int l = 0;
        int r = nums.length - 1;
        int mid = -1;
        while(l <= r){
            mid = l + (r - l)/2;
            if(target == nums[mid]) return mid;
            else if(target < nums[mid]){
                r = mid - 1;
            }
            else l = mid + 1;
        }
        return -1;
    }
}
