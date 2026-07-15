# 🟢 #119. Pascal's Triangle II

> **[LeetCode](https://leetcode.com/problems/pascals-triangle-ii/)** · 🟢 Easy · Solved on July 15, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Array` · `Dynamic Programming` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #119 in this repo |
| ⏱ **Runtime** | 0 ms |
| 💾 **Memory**  | 8.96
MB |

## 💡 Solution

```cpp
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

```

## ⚡ Performance

| Metric | Value | Percentile |
|--------|-------|------------|
| ⏱ Runtime  | `0 ms` | — |
| 💾 Memory   | `8.96
MB`  | — |

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
