# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return closestSum

        return closestSum