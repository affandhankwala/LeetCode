### 953: EASY
### STATUS: SOLVED

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) < 2: return True
        # Convert order into a dict with value correlating to position
        order_d = {}
        for i, letter in enumerate(order):
            order_d[letter] = i
        
        w1 = 0
        w2 = 1
        while w2 < len(words):
            word1 = words[w1]
            word2 = words[w2]
            i = 0
            determined = False
            while not determined:
                # See if word2 ran out. False if so (not in order)
                if i == len(word2): 
                    # See if both ran out
                    if i == len(word1):
                        determined = True
                    else: 
                        return False
                # See if word1 ran out. True since correct order
                elif i == len(word1): 
                    determined = True
                elif order_d[word1[i]] > order_d[word2[i]]: 
                    return False
                elif order_d[word1[i]] < order_d[word2[i]]:
                    determined = True
                i += 1
            w1 += 1
            w2 += 1
        return True