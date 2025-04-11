"""
    The function finds the k-th smalles or largest element in a list/sample in the simplest way possible.
    Which is to sort the list and return the k-th element.
    This is not the most efficient way, but it is the simplest.
    Parameters:
        nums (list[int]): The list of integers to find the k-th element from.
        k (int): The index of the element to find.
    Returns:
        int: The k-th smallest or largest element in the list.
"""
def findKthSmallestOrLargest(self, nums: list[int], k: int) -> int:
    return sorted(nums)[k]
