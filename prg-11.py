# Given a string s, find the length of the longest
# substring
#  without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character in the string
        char_index = {}

        # Start and end pointers of the sliding window
        start = 0
        max_length = 0

        for end in range(len(s)):
            # If the character is already in the window, update the start pointer
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            # Update the last index of the character
            char_index[s[end]] = end

            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length

# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))   # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))       # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))