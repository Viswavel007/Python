class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            # If we've already solved for this starting index, return cached result
            if start in memo:
                return memo[start]
            
            # Base Case: if we reach the end of the string, return a list with an empty string
            if start == len(s):
                return [""]
            
            res = []
            # Try every possible end index for a word starting at 'start'
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively find all ways to break the remaining substring
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        # Combine the current word with results from the suffix
                        sentence = (word + " " + sub).strip()
                        res.append(sentence)
            
            memo[start] = res
            return res

        return backtrack(0)
