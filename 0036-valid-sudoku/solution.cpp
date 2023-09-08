class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        const int cnt = 9;

        // 9 rows, 9 cols, 9 squares
        bool row[cnt][cnt] = {false};
        bool col[cnt][cnt] = {false};
        bool squares[cnt][cnt] = {false};

        // Check each row, col, square
        for (int r = 0; r < cnt; ++r)
        {
            for (int c = 0; c < cnt; ++c)
            {
                // Skip empty cell
                if (board[r][c] == '.') {
                    continue;
                }

                // Get index of current number
                // - '0' and -1 to get index within bounds
                int index = board[r][c] - '0' - 1;

                // Get square index
                int area = (r / 3) * 3 + (c / 3);

                // Check for duplicate
                if (row[r][index] || col[c][index] || squares[area][index]) {
                    return false;
                }

                // Mark as visited
                row[r][index] = true;
                col[c][index] = true;
                squares[area][index] = true;
            }
        }
        return true;
    }
};
