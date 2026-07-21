# 🟢 #168. Excel Sheet Column Title

> **[LeetCode](https://leetcode.com/problems/excel-sheet-column-title/)** · 🟢 Easy · Solved on July 21, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Math` · `String` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #168 in this repo |
| ⏱ **Runtime** | 0 ms |
| 💾 **Memory**  | 7.86
MB |

## 💡 Solution

```cpp
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res = "";
        while (columnNumber > 0) {
            columnNumber--;  // Shift to 0-indexed
            res += (char)('A' + columnNumber % 26);
            columnNumber /= 26;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

```

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
