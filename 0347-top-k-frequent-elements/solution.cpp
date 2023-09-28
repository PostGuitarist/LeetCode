class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        priority_queue<int, vector<int>, greater<int>> minHeap;
        unordered_map<int, int> count;

        while (!nums.empty()) {
            count[nums.back()]++;
            nums.pop_back();
        }

        for (auto it = count.begin(); it != count.end(); it++) {
            minHeap.push(it->second);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        for (auto it = count.begin(); it != count.end(); it++) {
            if (it->second >= minHeap.top()) {
                result.push_back(it->first);
            }
        }  

        return result;
    }
};
