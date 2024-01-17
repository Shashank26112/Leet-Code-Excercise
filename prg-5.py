# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1  # Initialize carry to 1 for the least significant digit

        for i in range(n - 1, -1, -1):
            current_sum = digits[i] + carry
            digits[i] = current_sum % 10  # Update the current digit
            carry = current_sum // 10  # Calculate the carry

            # If there is no carry, we can stop since further digits won't be affected
            if carry == 0:
                break

        # If there is still a carry after the loop, add a new digit at the beginning
        if carry > 0:
            digits.insert(0, carry)

        return digits


# Example usage:
solution = Solution()
digits1 = [1, 2, 3]
print(solution.plusOne(digits1))

digits2 = [4, 3, 2, 1]
print(solution.plusOne(digits2))

digits3 = [9]
print(solution.plusOne(digits3))  