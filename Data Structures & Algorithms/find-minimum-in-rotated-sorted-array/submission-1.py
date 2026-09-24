class Solution:
    def findMin(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] < arr[right]:
                return arr[left]

            mid = left + (right-left) // 2

            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid

        return arr[left]
        