# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal
# substring
#  consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trailing spaces
        s = s.strip()

        # Split the string by spaces
        words = s.split()

        # Return the length of the last word
        return len(words[-1])

# Example usage:
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))