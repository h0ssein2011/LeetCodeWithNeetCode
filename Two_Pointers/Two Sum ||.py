#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#Brute Force Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , 1
        searching = True
        while searching:
            while r < len(numbers):
                if target - numbers[r] == numbers[l]:
                    searching = False
                    return( l+1 ,r +1)
                r += 1
            l +=1
# better solution 
"""
1- sum left and right most values 
2- if sum of these is greater than target --> decrease the right as list is increasing 
3- 2- if sum of these is less than target --> increase the left as list is increasing 
4 - iterate till find the solution as there is always a answer!
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers)-1
        Searching = True
        while Searching:
            if numbers[l] + numbers[r] == target :
                return l +1 , r+1
                Searching = False
            
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else :
                l += 1
