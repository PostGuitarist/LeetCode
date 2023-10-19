class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1) {
            return 0;
        }

        int lowest = prices[0];
        int maxProfit = 0;

        for (auto price : prices) {
            if (price < lowest) {
                lowest = price;
            }
            else {
                if (price - lowest > maxProfit) {
                    maxProfit = price - lowest;
                }
            }
        }

        return maxProfit;
    }
};
