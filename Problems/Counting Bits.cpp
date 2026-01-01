//Return an array with a count of all the set bits of all numbers between the parameter, n, and 0

class Solution {
    public int[] countBits(int n) {
        //First create array with size n + 1
        //Loop through entire array with i starting at i to max index (n)
        //All odd numbers will have 1 more one than the numbers at index i/2;
        //All even numbers will have same number of 1's as index at i/2;
        int[] arr = new int[n + 1];
        arr[0] = 0;
        for(int i = 1; i < n + 1; i++){
            arr[i] = arr[i/2] + i % 2;
        }
        return arr;
    }
}
