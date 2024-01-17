# Given an array nums of size n, return the majority element.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize candidate and count
        candidate, count = nums[0], 1

        # Iterate through the array to find the majority element
        for num in nums[1:]:
            if count == 0:
                candidate, count = num, 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

# Example usage:
sol = Solution()
print(sol.majorityElement([3, 2, 3]))               # Output: 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))   # Output: 2