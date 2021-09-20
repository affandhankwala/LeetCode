//Calculates the sum of all elements in array between left and right parameters
//Implemented NumArray class to handle the queury

class NumArray {
    List<Integer> numbers = new ArrayList<Integer>();

    public NumArray(int[] nums) {
        for(int i = 0; i < nums.length; i++){
            numbers.add(nums[i]);
        }
    }
    
    public int sumRange(int left, int right) {
        int sum = 0;
        for(int i = left; i <= right; i++){
            sum += numbers.get(i);
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
