class Solution {
    public int[] plusOne(int[] digits) {
        int i = digits.length - 1;
        while (i >= 0) {
            if (digits[i] + 1 > 9) {
                // Carry
                digits[i] = 0;
                i--;
            }
            else {
                digits[i]++;
                return digits;
            }
        }
        // Create new int[] 
        int[] new_digits = new int[digits.length + 1];
        new_digits[0] = 1;
        for (int d = 0; d < digits.length; d ++) {
            new_digits[d + 1] = digits[d];
        }
        return new_digits;
    }
}