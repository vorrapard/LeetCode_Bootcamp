class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        def _findmax(left, right):
            max_index = left
            for i in range(left, right+1):
                if nums[i] > nums[max_index]:
                    max_index = i
            return max_index
        '''
        output = []
        n = len(nums)
        p_left = 0
        p_right = k-1
        first_max = 0
        second_max = 1
        for i in range(p_left, p_right+1):
            if nums[i] > nums[first_max]:
                second_max = first_max
                first_max = i
        output.append(nums[first_max])
        
        while p_right != n-1:
            print(nums[first_max], nums[second_max])
            p_left += 1
            p_right += 1
            if nums[p_right] > nums[first_max]:
                second_max = first_max
                first_max = p_right
            elif nums[p_right] > nums[second_max]:
                second_max = p_right
            if p_left-1 == first_max:
                first_max = second_max
                second_max = p_right if nums[p_right] > nums[p_left] else p_left
            elif p_left-1 == second_max:
                second_max = p_right if nums[p_right] > nums[p_left] else p_left
                        
            output.append(nums[first_max])

        return output


        
