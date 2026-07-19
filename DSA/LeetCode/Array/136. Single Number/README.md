# 🟢 #136. Single Number

> **[LeetCode](https://leetcode.com/problems/single-number/)** · 🟢 Easy · Solved on July 19, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Single Number](https://leetcode.com/problems/single-number/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Array` · `Bit Manipulation` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #136 in this repo |
| ⏱ **Runtime** | 0 ms |
| 💾 **Memory**  | 0.00
MB |

## 💡 Solution

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};

```

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
