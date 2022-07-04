# https://leetcode.com/problems/valid-parentheses/
# Brute Force solution
# Still has problem with order 
class Solution:
    def isValid(self, s: str) -> bool:
        p , k , b = False , False ,False
        p_count = (s.count('(') + s.count(')'))
        k_count = (s.count('{') + s.count('}'))
        b_count = (s.count('[') + s.count(']'))
        
        if  p_count % 2 ==0 or p_count ==0:
            p = True
            
        if  k_count % 2 ==0 or k_count ==0:
            k = True
            
        if b_count % 2 ==0 or b_count ==0:
            b =True
        return( p *b*k )
    
# second approach still has bug!
# remove all extra charachter and check it is valid or not
class Solution:
    def isValid(self, s: str) -> bool:
        p_list =[c for c in s if c in ('(',')')]
        b_list =[c for c in s if c in ('{','}')]
        k_list =[c for c in s if c in ('[',']')]
        
        if (''.join(p_list) == '()' or len(p_list) == 0) and  \
        (''.join(b_list) == '{}' or len(b_list) == 0) and \
        (''.join(k_list) == '[]' or len(k_list) == 0):
            return True
        return False
