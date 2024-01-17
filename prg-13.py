# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of the merged array
        index = m + n - 1
        i, j = m - 1, n - 1

        # Merge nums1 and nums2 in descending order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
sol.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nums2 = [1]
sol.merge(nums2, 0, [0], 1)
print(nums2)  # Output: [1]

nums3 = [0]
sol.merge(nums3, 0, [1], 1)
print(nums3)  # Output: [1]