class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxScore = 0
        currNum = -1
        for divisor in divisors:
            curr = 0
            for num in nums:
                if num % divisor == 0:
                    curr += 1
            if curr > maxScore or (curr == maxScore and divisor < currNum):
                maxScore = curr
                currNum = divisor
        return currNum if currNum != -1 else min(divisors)

