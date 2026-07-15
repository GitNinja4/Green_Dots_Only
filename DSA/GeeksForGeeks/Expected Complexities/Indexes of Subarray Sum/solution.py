class Solution {
  public:
    vector<int> subarraySum(vector<int> &arr, int target) {
        int s = 0;
        long long curr_sum = 0;
        int n = arr.size();

        for (int e = 0; e < n; e++) {
            // Expand the window by adding the current element
            curr_sum += arr[e];

            // Shrink the window from the left if the current sum exceeds the target
            while (curr_sum > target && s < e) {
                curr_sum -= arr[s];
                s++;
            }

            // Check if the current window sum matches the target
            if (curr_sum == target) {
                return {s + 1, e + 1}; // Return 1-based indices
            }
        }
        
        // Return {-1} if no continuous subarray is found
        return {-1};
    }
};