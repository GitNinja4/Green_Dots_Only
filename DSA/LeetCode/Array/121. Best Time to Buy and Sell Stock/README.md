# 🟢 #121. Best Time to Buy and Sell Stock

> **[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)** · 🟢 Easy · Solved on July 18, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 🏷 **Difficulty** | 🟢 Easy |
| 🧩 **Topics** | `Array` · `Dynamic Programming` |
| 💻 **Language** | C++ |
| 🔢 **Solve #** | #121 in this repo |
| ⏱ **Runtime** | 0 ms |
| 💾 **Memory**  | 0.00
MB |

## 💡 Solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;
        
        for (int price : prices) {
            if (price < min_price) {
                min_price = price;
            } else if (price - min_price > max_profit) {
                max_profit = price - min_price;
            }
        }
        
        return max_profit;
    }
};
```

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
