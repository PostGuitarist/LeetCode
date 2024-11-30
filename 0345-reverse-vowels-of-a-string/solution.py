class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        seenVowel = []
        tempS = ""
        newS = ""

        for c in s:
            if c not in vowel:
                tempS += c
            else:
                tempS += "_"
                seenVowel.append(c)
            
        seenVowel.reverse()
        count = 0

        for c in tempS:
            if c == "_":
                newS += seenVowel[count]
                count += 1
            else:
                newS += c
        
        return newS

