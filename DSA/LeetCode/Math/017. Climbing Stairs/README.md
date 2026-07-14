# ⚡ #17. Climbing Stairs

> **[LeetCode](https://leetcode.com/problems/climbing-stairs/)** · — · Improved on July 14, 2026

> 🔄 **Improved solution** — see [commit history](https://leetcode.com/problems/climbing-stairs/) for the previous attempt.

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |
| 🏷 **Difficulty** | — |
| 🧩 **Topics** | — |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #17 in this repo |
| ⏱ **Runtime** | 2
ms |
| 💾 **Memory**  | 8.39
MB |

## 💡 Solution

```cpp
class Solution {
public:
    int climbStairs(int n, unordered_map<int, int>& memo) {

        if (n == 0 || n == 1) {
            return 1;
        }
        
        if (memo.find(n) == memo.end()) {
            memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo);
        }
        return memo[n];
    }

    int climbStairs(int n) {
        unordered_map<int, int> memo;
        return climbStairs(n, memo);
    }
};
```

## ⚡ Performance

| Metric | Value | Percentile |
|--------|-------|------------|
| ⏱ Runtime  | `2
ms` | — |
| 💾 Memory   | `8.39
MB`  | — |

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
