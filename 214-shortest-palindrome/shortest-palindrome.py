class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Combine string with its reverse, using a separator
        # This creates a pattern where the prefix function finds 
        # the longest prefix that is also a suffix.
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        # Build KMP table (Prefix Function)
        # pi[i] is the length of the longest proper prefix of combined[:i+1] 
        # that is also a suffix of combined[:i+1]
        n = len(combined)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        
        # Longest palindromic prefix length is the last value in pi
        longest_palindromic_prefix_len = pi[-1]
        
        # Add the remaining non-palindromic part (reversed) to the front
        suffix_to_add = s[longest_palindromic_prefix_len:]
        return suffix_to_add[::-1] + s
