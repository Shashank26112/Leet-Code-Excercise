class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the complement of each element along with its index
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_dict:
                # Return the indices of the two numbers that add up to the target
                return [num_dict[complement], i]

            # If complement not found, store the current number and its index in the dictionary
            num_dict[num] = i

        # No solution found
        return None


# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6)) 