class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row(rowIndex + 1, 1);
        long long current_val = 1; // Use long long to prevent integer overflow during multiplication
        
        for (int j = 1; j < rowIndex; ++j) {
            current_val = current_val * (rowIndex - j + 1) / j;
            row[j] = current_val;
        }
        
        return row;
    }
};
