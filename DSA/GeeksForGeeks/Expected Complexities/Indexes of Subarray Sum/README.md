# ⚡ Indexes of Subarray Sum

> **[GeeksForGeeks](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1)** · — · Solved on July 16, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Indexes of Subarray Sum](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1) |
| 🏷 **Difficulty** | — |
| 🧩 **Topics** | `Expected Complexities` · `Expected Complexities` · `Company TagsAmazonFacebookGoogleVisa` · `Company Tags` · `Company Tags` · `Amazon` · `Facebook` · `Google` · `Visa` · `Topic Tags` |
| 💻 **Language** | Python 3 |
| 🔢 **Solve #** | Platform problem number unavailable |



## 💡 Solution

```py
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
```

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
