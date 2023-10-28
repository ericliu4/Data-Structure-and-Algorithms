class Solution:
    def countVowelPermutation(self, n: int) -> int:
        aCount = [1]*n
        eCount = [1]*n
        iCount = [1]*n
        oCount = [1]*n
        uCount = [1]*n
        MOD = 10**9+7
        for i in range(1,n):
            aCount[i] = (eCount[i-1] + iCount[i-1] + uCount[i-1])%MOD
            eCount[i] = (aCount[i-1] + iCount[i-1])%MOD
            iCount[i] = (eCount[i-1] + oCount[i-1])%MOD
            oCount[i] = (iCount[i-1])%MOD
            uCount[i] = (iCount[i-1]+oCount[i-1])%MOD
        return (aCount[n-1] + eCount[n-1] + iCount[n-1] + oCount[n-1] + uCount[n-1])%MOD
