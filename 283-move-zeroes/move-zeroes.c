void moveZeroes(int* nums, int numsSize) {
    int left = 0;  // position where next non-zero should go

    for (int right = 0; right < numsSize; right++) {
        if (nums[right] != 0) {
            // swap only when needed
            if (left != right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
            left++;
        }
    }
}