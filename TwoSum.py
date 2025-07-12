class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Empty dictionary
        for i in range(len(nums)):  
            num = nums[i]  # Current number
            complement = target - num  # Complement jo chahiye
            if complement in seen:  # Agar complement dictionary mein hai
                return [seen[complement], i]  # Complement ka index aur current index
            seen[num] = i  # Current number aur uska index dictionary mein daal do
        return []  # Agar koi solution na mile
