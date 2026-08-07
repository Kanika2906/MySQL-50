class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = sum(nums)
        ex_sum = n*(n+1)//2
        return ex_sum - sum1

    #time complexity = O(n)
    #space = O(1)
