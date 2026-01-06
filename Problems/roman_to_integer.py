### 13. EASY
### STATUS: SOLVED
### BEATS: 70%

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        order = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        if len(s) == 0: return 0
        if len(s) == 1: return order[s[0]]
        
        i, j, total = 0, 1, 0
        while (i < len(s)):
            # Check if j valid
            if j < len(s):
                value_i = order[s[i]]
                value_j = order[s[j]]
                if value_j > value_i:
                    # Subtract value_i from value_j
                    total += (value_j - value_i)
                    # Set i = j + 1 and j as j + 2
                    i = j + 1
                    j += 2
                # In order so just add value at i
                else:
                    total += value_i
                    # Increment both pointers by 1
                    i += 1
                    j += 1
            else:
                # Last element, just add it
                total += order[s[i]]
                i += 1
        return total
        



s = "MCMXCIV"
a = Solution()
print(a.romanToInt(s))