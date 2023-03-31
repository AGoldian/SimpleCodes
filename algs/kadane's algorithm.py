class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prev_sum = 0
        beg = 0     # index of start subarray
        end = 0     # index of end subarray
        answer = nums[0]

        for i in range(len(nums)):
            if prev_sum + nums[i] > nums[i]:
                prev_sum += nums[i]
            else:
                prev_sum = nums[i]
                beg = i
            
            if prev_sum >= answer:
                answer = prev_sum
                end = i

        return answer, beg, end



df = [-2,1,-3,4,-1,2,1,-5,4]
sum_subarray, index_of_start, index_of_end = Solution().maxSubArray(df)

print(f'Sum of subarray = {sum_subarray}\nSubarray: {df[index_of_start:index_of_end]}')