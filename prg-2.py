# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Handle the case of an empty array
        if not nums:
            return 0

        # Initialize variables
        unique_count = 1  # At least one unique element (the first one)

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Update the array in-place and increase the count of unique elements
                nums[unique_count] = nums[i]
                unique_count += 1

        return unique_count


# Example usage:
solution = Solution()
nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])