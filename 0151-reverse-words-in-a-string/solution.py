class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        rev = []

        for i in range(len(words) - 1, -1, -1):
            rev.append(words[i])

            if i != 0:
                rev.append(" ")

        return "".join(rev)
