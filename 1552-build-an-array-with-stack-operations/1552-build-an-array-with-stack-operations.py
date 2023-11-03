class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        index = 0
        m = len(target)
        count = 1
        while (index != m):
            ans.append("Push")
            if count != target[index]:
                ans.append("Pop")
            else:
                index += 1
            count += 1
        return ans

            
