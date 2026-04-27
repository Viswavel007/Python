from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        res = []
        
        # We only need to start the sliding window from 0 up to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            words_used = 0
            
            # Slide the window across the string in increments of word_len
            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_counts:
                    current_counts[word] += 1
                    words_used += 1
                    
                    # If we have too many instances of a word, shift 'left'
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left : left + word_len]
                        current_counts[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # If the number of words matches, we found a valid index
                    if words_used == num_words:
                        res.append(left)
                else:
                    # Not a valid word, reset the window
                    current_counts.clear()
                    words_used = 0
                    left = right
                    
        return res
