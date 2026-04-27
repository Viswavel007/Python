from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        # Dictionary to store combinations of words that can be formed 
        # by changing one letter. Key: pattern (e.g., "h*t")
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        
        # Queue for BFS: (current_word, level)
        queue = deque([(beginWord, 1)])
        # Visited to avoid cycles
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(L):
                # Intermediate state for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                # Next states are all words that share the same intermediate state
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                
                # Clear the pattern list once visited to save time in future iterations
                all_combo_dict[intermediate_word] = []
                
        return 0
