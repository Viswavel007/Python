class Solution(object):
    def isPalindrome(self, x):
        rev=0
        if x<0 or (x%10==0 and x!=0):
            return False 
        while x>rev:
            rev=rev*10+x%10
            x//=10
        return rev==x or rev//10==x
        