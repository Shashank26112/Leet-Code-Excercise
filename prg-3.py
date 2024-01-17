# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize variable to track the number of elements not equal to val
        not_val_count = 0

        # Iterate through the array
        for num in nums:
            # Check if the current element is not equal to val
            if num != val:
                # Update the array in-place and increase the count of elements not equal to val
                nums[not_val_count] = num
                not_val_count += 1

        return not_val_count


# Example usage:
solution = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = solution.removeElement(nums1, val1)
print(k1, nums1[:k1])

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = solution.removeElement(nums2, val2)
print(k2, nums2[:k2])