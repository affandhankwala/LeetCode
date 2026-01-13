//Finds the missing number in array. This is assuming that array will have all elements from 1 - array.size

class Solution {
    public int missingNumber(int[] nums) {
        //Calculate sum of all numbers in num
        //Subtract each element. Ending result should be missing number
        
        //Sum of all elements:
        // n(n+1)/2
        
        int sum = (nums.length * (nums.length + 1)) / 2;
        
        //Loop through entire array
        for(int i = 0; i < nums.length; i++){
            //Subtract element
            sum -= nums[i];
        }
        return sum;
        
    }
}
