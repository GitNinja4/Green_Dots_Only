# ⚡ The FizzBuzz Program

> **[GeeksForGeeks](https://www.geeksforgeeks.org/problems/the-fizzbuzz-program/1)** · — · Solved on July 19, 2026

## 📋 Details

| Field | Value |
|-------|-------|
| 🔗 **Problem** | [The FizzBuzz Program](https://www.geeksforgeeks.org/problems/the-fizzbuzz-program/1) |
| 🏷 **Difficulty** | — |
| 🧩 **Topics** | `Expected Complexities` · `Expected Complexities` · `Topic Tags` · `Topic Tags` · `python-conditionals` · `CPP` · `Java` · `python` · `Related Articles` · `Related Articles` |
| 💻 **Language** | Python 3 |
| 🔢 **Solve #** | Platform problem number unavailable |



## 💡 Solution

```py
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    // code here
    if (n % 3 == 0 && n % 5 == 0){
        cout << "FizzBuzz";
    }else if (n % 3 == 0){
        cout << "Fizz";
    }else if (n % 5 == 0){
        cout << "Buzz";
    }else{
        cout << n;
    }
    

    return 0;
}
```

## 📝 Notes

<!-- Add your approach, key observations, or edge cases here -->

---
*Tracked by [GreenDots](https://github.com/GitNinja4/GreenDots) 🟢*
