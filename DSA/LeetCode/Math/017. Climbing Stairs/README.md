# 🟢 #17. Climbing Stairs

> **[LeetCode](https://leetcode.com/problems/climbing-stairs/)** · 🟢 Easy · Improved on July 14, 2026

> 🔄 **Improved solution** — see [commit history](https://leetcode.com/problems/climbing-stairs/) for the previous attempt.

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Math` · `Dynamic Programming` · `Memoization` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #17 in this repo |
| ⏱ **Runtime** | 0 ms |


## 💡 Solution

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return climbStairs(n-1) + climbStairs(n-2);
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
