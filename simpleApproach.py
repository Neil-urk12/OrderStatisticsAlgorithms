class SimplestApproach:
    def findKthSmallestOrLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(left, right):

