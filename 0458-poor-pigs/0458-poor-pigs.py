class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest//minutesToDie
        return ceil(log2(buckets)/log2(tests+1))