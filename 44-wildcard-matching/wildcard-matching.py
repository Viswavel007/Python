class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = p_ptr = 0
        star_idx = -1
        s_tmp_ptr = -1
        
        while s_ptr < len(s):
            # 1. Direct match or '?' wildcard
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            
            # 2. '*' wildcard found: record position and try matching 0 characters first
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_ptr = s_ptr
                p_ptr += 1
            
            # 3. No match, but a '*' was seen previously: backtrack
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_tmp_ptr += 1
                s_ptr = s_tmp_ptr
            
            # 4. No match and no previous '*'
            else:
                return False
        
        # Check if remaining characters in pattern are all '*'
        return all(x == '*' for x in p[p_ptr:])
