class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        B = list()
        
        if (len(nums) % 2 == 1):
            count = nums.count(nums[0])
            if (count > len(nums) / 2):
                return nums[0]
            else:
                del nums[0]
        for i in range(0, int(len(nums)/2), 1):
            if (nums[2*(i)] == nums[2*(i)+1]):
                B.append(nums[2*i])      
        return self.majorityElement(B)
        