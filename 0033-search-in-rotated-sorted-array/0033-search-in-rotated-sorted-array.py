class Solution:
    def search(self, nums, target):
        """
        Search for a target in a rotated sorted array using binary search.

        Args:
        - nums (List[int]): The rotated sorted array.
        - target (int): The target value to search for.

        Returns:
        - int: The index of the target if found, otherwise -1.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# Example usage:
solution = Solution()

nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(solution.search(nums1, target1))  # Output: 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(solution.search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(solution.search(nums3, target3))  # Output: -1
