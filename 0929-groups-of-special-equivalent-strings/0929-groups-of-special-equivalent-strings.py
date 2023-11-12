class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = 0
        seen = set()
        for index, word in enumerate(words):
            if word in seen:
                continue
            wordDict1 = collections.Counter()
            wordDict2 = collections.Counter()
            for i, ch in enumerate(word):
                if i %2 == 0:
                    wordDict1[ch] += 1
                else:
                    wordDict2[ch] += 1
            for nextword in words[index+1:]:
                if nextword not in seen:
                    NextwordDict1 = collections.Counter()
                    NextwordDict2 = collections.Counter()
                    for i, ch in enumerate(nextword):
                        if i %2 == 0:
                            NextwordDict1[ch] += 1
                        else:
                            NextwordDict2[ch] += 1
                    if NextwordDict1 == wordDict1 and NextwordDict2 == wordDict2:
                        seen.add(nextword)
            
            seen.add(word)
            groups += 1



        return groups