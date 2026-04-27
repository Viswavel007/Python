class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            # If adding the next word exceeds maxWidth (word lengths + at least 1 space between words)
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces for the completed line
                for i in range(maxWidth - num_of_letters):
                    # Use modulo to distribute spaces from left to right
                    # (len(cur)-1 or 1) handles the single-word-in-line case
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            
            cur.append(w)
            num_of_letters += len(w)
        
        # Handle the last line: left-justified, single space between words, pad right
        last_line = " ".join(cur)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return res
