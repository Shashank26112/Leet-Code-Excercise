# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Sort the strings to ensure the common prefix is at the beginning of the first and last strings
        strs.sort()

        # Take the first and last strings after sorting
        first_str, last_str = strs[0], strs[-1]

        common_prefix = []

        # Iterate through characters in the first string
        for i in range(len(first_str)):
            # Check if the character is the same in the last string
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                # If characters are not the same, break the loop
                break

        return "".join(common_prefix)


# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))