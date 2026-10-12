class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def majority(left, right):
            # Base case
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # Find majority in left and right halves
            left_major = majority(left, mid)
            right_major = majority(mid + 1, right)

            # If both halves agree, return it
            if left_major == right_major:
                return left_major

            # Count occurrences in the current range
            left_count = 0
            right_count = 0

            for i in range(left, right + 1):
                if nums[i] == left_major:
                    left_count += 1
                if nums[i] == right_major:
                    right_count += 1

            if left_count > right_count:
                return left_major
            else:
                return right_major

        return majority(0, len(nums) - 1)