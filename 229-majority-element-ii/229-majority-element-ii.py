class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output_list = []
        for num in set(nums):
            if nums.count(num) > (len(nums) / 3):
                output_list.append(num)
        return output_list