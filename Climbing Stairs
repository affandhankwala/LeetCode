//Identifies the total possible ways to climb n stairs given one can only traverse 1 or 2 steps at a time. 

class Solution {
    public int climbStairs(int n) {
        int[] arr = new int[n + 1];
        if(n == 0) return 1;
        if(n == 1) return 1;
        if(n == 2) return 2;
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 2;
        for(int i = 3; i < arr.length; i++){
            arr[i] = arr[i - 1] + arr[i - 2];
        }
        return arr[n];
        
    }
}
