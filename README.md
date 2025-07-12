**Approach (Hash Map - Beginner Friendly)**
Ab ek smarter tareeka dekhte hain jo fast hai aur ek hi baar mein list ko dekhta hai. Isme hum ek dictionary use karenge (jo Python mein key-value pairs store karta hai). Idea yeh hai:

Har number ke liye, hum check karenge ki target - number wala number pehle dekha hai ya nahi.
Agar dekha hai, toh dono ke index return kar denge.
Nahi toh, current number aur uska index dictionary mein daal denge.
Python Code (Hash Map):

**def twoSum(nums, target):
    seen = {}  # Empty dictionary banaya
    for i in range(len(nums)):  # Har number ke liye loop
        num = nums[i]  # Current number
        complement = target - num  # Yeh check karna hai ki (target - num) hai ya nahi
        if complement in seen:  # Agar complement dictionary mein hai
            return [seen[complement], i]  # Uska index aur current index return karo
        seen[num] = i  # Current number aur uska index dictionary mein daal do
    return []  # Agar koi solution na mile**

**Kaise Kaam Karta Hai?**

nums = [2, 7, 11, 15], target = 9 ke liye:
i = 0: num = 2, complement = 9 - 2 = 7
seen mein 7 nahi hai, toh seen = {2: 0} daal do.
i = 1: num = 7, complement = 9 - 7 = 2
seen mein 2 hai (index 0 pe), toh return [seen[2], 1] = [0, 1].
Aise hi aage chalega agar zarurat pade.

**Fayda Kya Hai?**

Yeh sirf ek baar list ko dekhta hai, toh yeh fast hai (O(n) time).
Dictionary use karne se hum instantly check kar sakte hain ki complement hai ya nahi.
Time Complexity: O(n) (ek hi loop).
Space Complexity: O(n) (dictionary mein numbers store karte hain).

Example Se Samjho
nums = [3, 2, 4]
target = 6
nums = [3, 2, 4]
target = 6
 Chalao hash map wala code:
 seen = {}
 i = 0: num = 3, complement = 6 - 3 = 3, seen = {3: 0}
 i = 1: num = 2, complement = 6 - 2 = 4, seen = {3: 0, 2: 1}
 i = 2: num = 4, complement = 6 - 4 = 2, seen mein 2 hai, return [seen[2], 2] = [1, 2]
