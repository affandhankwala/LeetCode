class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() - 1;
        while (i >= 0){
            if (digits[i] + 1 > 9) {
                // Carry
                digits[i] = 0;
                i --;
            }
            else {
                digits[i] ++;
                return digits;
            }
        }
        // Create a new vector with 1 as first element and deep copy of digits
        vector<int> new_digits;
        new_digits.push_back(1);
        for (int d : digits) {
            new_digits.push_back(d);
        }
        return new_digits;
    }
};