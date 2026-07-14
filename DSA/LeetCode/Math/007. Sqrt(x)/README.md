# 🟢 #7. Sqrt(x)

> **[LeetCode](https://leetcode.com/problems/sqrtx/)** · 🟢 Easy · Improved on July 14, 2026

> 🔄 **Improved solution** — see [commit history](https://leetcode.com/problems/sqrtx/) for the previous attempt.

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Math` · `Binary Search` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #7 in this repo |
| ⏱ **Runtime** | 0 ms |


## 💡 Solution

```cpp
class Solution {
public:
    int mySqrt(int x) {
        // Base cases for 0 and 1
        if (x < 2) {
            return x;
        }
        
        int left = 1;
        int right = x / 2;
        int ans = 0;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // Use division (x / mid) instead of multiplication (mid * mid)
            // to completely avoid integer overflow issues
            if (mid <= x / mid) {
                ans = mid;       // Keep track of the closest valid answer
                left = mid + 1;  // Try to find a larger value
            } else {
                right = mid - 1; // mid is too large, search the lower half
            }
        }
        
        return ans ;
    }
};

```

## ⚡ Performance

| Metric | Value | Percentile |
|--------|-------|------------|
| ⏱ Runtime  | `0 ms` | — |

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
