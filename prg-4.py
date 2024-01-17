# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check if the target is equal to the middle element
            if nums[mid] == target:
                return mid

            # If the target is smaller, search in the left half
            elif nums[mid] > target:
                right = mid - 1

            # If the target is larger, search in the right half
            else:
                left = mid + 1

        # If the target is not found, return the index where it would be inserted
        return left


# Example usage:
solution = Solution()
nums1, target1 = [1, 3, 5, 6], 5
print(solution.searchInsert(nums1, target1))

nums2, target2 = [1, 3, 5, 6], 2
print(solution.searchInsert(nums2, target2))

nums3, target3 = [1, 3, 5, 6], 7
print(solution.searchInsert(nums3, target3))