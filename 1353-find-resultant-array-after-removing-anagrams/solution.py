class Solution:
    def anagrams(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)

    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if not self.anagrams(words[i], words[i-1]):
                result.append(words[i])
        return result
