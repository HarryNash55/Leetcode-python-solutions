class Solution:
    def twoSum(self, nums, target):
        num1 = 0
        num2 = 0
        result = []
        while True:
            if num1 != num2:
                if nums[num1] + nums[num2] == target:
                    result.append(num1)
                    result.append(num2)
                    return result
            if num2 != (len(nums) - 1):
                num2 += 1
            else:
                num2 = 0
                num1 += 1
#This solution had 8518ms of runtime, beating only 5% of solutions
