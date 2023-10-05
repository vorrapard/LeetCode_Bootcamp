class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        #Runtime
        if len(set(nums)) != n:
            return True
        return False

        #Memory Efficient
        nums.sort()
        print(nums)
        for i in range(n):
            if (nums[i-1] == nums[i]):
                return True        
        return False        
