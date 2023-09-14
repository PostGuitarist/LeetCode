class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int size = matrix.size();
        int n = matrix[0].size();
        int start = 0;
        int end = size * n - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            int e = matrix[mid/n][mid%n];
            
            if (target < e) {
                end = mid - 1;
            }
            else if (target > e) {
                start = mid + 1;
            }
            else {
                return true;
            }
        }
        
        return false;
    }
};
