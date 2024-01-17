# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a set to store unique elements
        unique_elements = set()

        for num in nums:
            # If the element is already in the set, it's a duplicate
            if num in unique_elements:
                return True
            # Otherwise, add the element to the set
            unique_elements.add(num)

        # No duplicates found
        return False

# Example usage:
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))                    # Output: True
print(sol.containsDuplicate([1, 2, 3, 4]))                    # Output: False
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))