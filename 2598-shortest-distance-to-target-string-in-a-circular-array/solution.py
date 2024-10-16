class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1

        min_distance = len(words) - 1

        for index, word in enumerate(words):
            if word == target:
                if index < startIndex:
                    distance = min(startIndex - index, index + len(words) - startIndex)
                else:
                    distance = min(index - startIndex, startIndex + len(words) - index)
                min_distance = min(distance, min_distance)
        return min_distance
