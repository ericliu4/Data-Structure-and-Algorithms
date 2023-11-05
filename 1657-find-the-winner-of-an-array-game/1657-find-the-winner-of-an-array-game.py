class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr = arr[0]
        count = 0
        for index, element in enumerate(arr[1:], start=1):
            if element > curr:
                count = 1
                if count == k:
                    return element
                curr = element
            else:
                count += 1
                if count == k:
                    return curr
        return curr

