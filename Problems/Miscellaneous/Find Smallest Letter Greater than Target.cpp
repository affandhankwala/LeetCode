//Find the smallest letter that is greater than the target letter.
//The letters also wrap around meaning if target = z and array = ['a', 'b'] then we expect to return 'a';
//All letters are lowercase

class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        //Perform binary search to find the smallest larger number
        //But they wrap around...
        // int l = 0;
        // int r = letters.length - 1;
        // int mid = 0;
        // char largest = '0';
        // while(true){
        //     mid = l + (r - l)/2;
        
        //Iterative search first
        int i = 0; 
        while(i < letters.length){
            if(letters[i] > target){
                return letters[i];
            }
            i++;
        }
        //At this point i has gone through entire array and none of elements were larger. 
        //Loop through once more but compare to the uppercase of letters
        i = 0;
        while(i < letters.length){
            if(letters[i] > Character.toUpperCase(target)) return letters[i];
            i++;
        }
        
        //Dont think it'll ever hit this point but included a character return of '0' to indicate error
        return '0';
    }
}
