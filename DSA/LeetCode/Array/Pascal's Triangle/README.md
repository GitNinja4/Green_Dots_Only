# 🟢 Pascal's Triangle

> **[LeetCode](https://leetcode.com/problems/pascals-triangle/)** · 🟢 Easy · Solved on July 15, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Array` · `Dynamic Programming` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | Platform problem number unavailable |
| ⏱ **Runtime** | 0
ms |
| 💾 **Memory**  | 0.00
MB |

## 💡 Solution

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        
        for (int i = 0; i < numRows; ++i) {
            // Create a row of size (i + 1) filled with 1s
            vector<int> row(i + 1, 1);
            
            // Fill in the inner elements using the row directly above
            for (int j = 1; j < i; ++j) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
            
            // Add the completed row to the triangle
            triangle.push_back(row);
        }
        
        return triangle;
    }
};

```

## ⚡ Performance

| Metric | Value | Percentile |
|--------|-------|------------|
| ⏱ Runtime  | `0
ms` | — |
| 💾 Memory   | `0.00
MB`  | — |

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
