//This program takes the role of purchasing and selling a stock based on the prices of said stock in an array. Returns the greatest profit possible

class Solution {
    public int maxProfit(int[] prices) {
        int low = Integer.MAX_VALUE;
        int profit = 0;
        for (int price:prices){
            if(price < low) low = price;
            else if(price - low > profit) profit = price - low;
        }
        return profit;
    }
}
