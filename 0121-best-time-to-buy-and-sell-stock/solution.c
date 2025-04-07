int maxProfit(int* prices, int pricesSize) {
    int least = INT_MAX;
    int profit = 0;
    int pIfSold = 0;

    for (int i = 0; i < pricesSize; i++) {
        if(prices[i] < least) {
            least = prices[i];
        }

        pIfSold = prices[i] - least;

        if (profit < pIfSold) {
            profit = pIfSold;
        }
    }

    return profit;
}
