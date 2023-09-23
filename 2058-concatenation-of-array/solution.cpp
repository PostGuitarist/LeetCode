class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> numstwo;

        for (int i = 0; i < nums.size(); i++) {
            numstwo.push_back(nums[i]);
        }
        for (int i = 0; i < nums.size(); i++) {
            numstwo.push_back(nums[i]);
        }

        return numstwo;
    }
};
