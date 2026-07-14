# 🟢 #1. Plus One

> **[LeetCode](https://leetcode.com/problems/plus-one/)** · 🟢 Easy · Solved on July 14, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Plus One](https://leetcode.com/problems/plus-one/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `array` · `math` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #1 in this repo |
| ⏱ **Runtime** | 0
ms (beats 100.0%) |
| 💾 **Memory**  | 11.6 MB (beats 62.3%) |

## 💡 Solution

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; --i){
            if (digits[i] < 9){
            digits[i]++;
            return digits;
            }
        digits[i] = 0;
        }
    // digits.insert(digits.begin(), 1);
    // return digits;
    digits[0] = 1;
    digits.push_back(0);
    return digits;
    }
};
```

## ⚡ Performance

| Metric | Value | Percentile |
|--------|-------|------------|
| ⏱ Runtime  | `0
ms` | Beats 100.0% |
| 💾 Memory   | `11.6 MB`  | Beats 62.3% |

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
