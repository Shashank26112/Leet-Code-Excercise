#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Initialize variables to store the result indices
    int* result = NULL;
    *returnSize = 0;

    // Iterate through the array
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            // Check if the current pair sums up to the target
            if (nums[i] + nums[j] == target) {
                // Allocate memory for the result array and store the indices
                result = (int*)malloc(2 * sizeof(int));
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }

   int main() {
    // Example usage
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, 4, target, &returnSize);

    // Process the result or print it
    if (result != NULL) {
        for (int i = 0; i < returnSize; i++) {
            printf("%d ", result[i]);
        }
        free(result); // Free the allocated memory
    } else {
        printf("No solution found.");
    }

    return 0;
}

    return result;
}
