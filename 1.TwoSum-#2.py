#Looked at hint 2
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            seen.update({num: i })
        for i in range(len(nums)):
            temp = (target - nums[i]) 
            if temp in seen:
                if seen.get(temp) != i:
                    solutions = []
                    solutions.append(seen.get(temp))
                    solutions.append(i)
                    return solutions
#This solution had a runtime of 5ms beating 50% of solutions
#This solution used 13.44mb beating 15.97% of solutions
