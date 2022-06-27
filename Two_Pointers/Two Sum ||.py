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
