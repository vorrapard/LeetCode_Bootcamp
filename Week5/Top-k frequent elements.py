
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = []
        if n == 1:
            return [nums[0]]

        myDict = collections.Counter(nums)
        index = sorted(myDict.values(), reverse=True)
        for number in myDict:
            if myDict[number] >= index[k-1]:
                output.append(number)

        return output     
