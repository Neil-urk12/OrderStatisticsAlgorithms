import random #For random selecting of pivot

"""
Implements the QuickSelect algorithm to efficiently find the k-th smallest element
in an unordered array.

The Quick Select algorithm uses a randomized pivot strategy and partitioning (similar to QuickSort)
to narrow down the search space in expected linear time complexity (O(n) on average, O(n^2) in the worst case).

The Quck Select algorithm is very efficient for finding the k-th smallest element in an unordered array.

    -> int, this means that this function returns an integer
"""
def quick_select(arr: list[int], k: int) -> int: # I explicitly stated the data types
    """
    Find the k-th smallest element in the array using Quick Select.

    The parameter nums, is a array of unsorted elements.
    The parameter k determines which smallest element to find

    Returns:
    - The k-th smallest element in the array.

    Raises:
    - ValueError or IndexError if k is out of bounds.
    """

    if k < 0 or k >= len(arr):
        raise ValueError(f"k must be between 0 and {len(arr) - 1}, but got {k}")
    if not arr:
        raise ValueError("Input array cannot be empty")

    # Call the helper function to start the Quick Select process
    # The helper function handles the selecting of random pivots
    return pivot_selector(arr, k, 0, len(arr) - 1)

def pivot_selector(arr, k, left, right):
    """
    Recursively finds the k-th smallest element within the array/subarray(left or right)

    This is the most important part of the quick select algorithm.
    It selects a random pivot and partitions the array around it,
    and then recursively searches in the appropriate partition based on the pivot's final position.

    Args:
        arr: the array or subarray to search within
        k: the index of the k-th smallest element to find
        left: the starting index of the current subarray to search within
        right: the ending index of the current subarray to search within

    Returns:
        The k-th smallest element in the array/subarray.
        It returns the smallest element in the array after all recursive calls have returned.
    """

    # Base Case: If the array contains only one element, return that element
    if left == right:
        return arr[left]

    # --- Pivot Selection ---
    # Select a random pivot index within the subarray [left or right]
    # The selection of random pivots helps avoid the worst-case O(n^2) performance on sorted/almost sorted data.
    pivot_index = random.randint(left, right)

    # --- Partitioning ---
    # Partition the array around the pivot
    # The partition function rearranges the elements such that:
        # Elements smaller than the pivot are placed to the left of the pivot
        # Elements greater than the pivot are placed to the right of the pivot
        # It returns the final index where the pivot element ends up after partitioning
    pivot_index = partition(arr, left, right, pivot_index)

    # --- Recursion / Checking of results ---
    # If the pivot is at the k-th position, return the pivot
    if k == pivot_index:
        return arr[k]
    # If the k-th position is on the left side of the pivot, recurse on the left
    elif k < pivot_index:
        return pivot_selector(arr, k, left, pivot_index - 1)
    # If the k-th position is on the right side of the pivot, recurse on the right
    else:
        return pivot_selector(arr, k, pivot_index + 1, right)

def partition(arr, left, right, pivot_index):
    """
    Partitions the left or right subarray arr around the element at pivot_index

    This function rearranges the elements in the subarray such that all elements
    smaller than the pivot are placed to the left, and all elements greater than
    the pivot are placed to the right. It returns the final index where the pivot
    element ends up after partitioning.

    Args:
        arr (list): The array to be partitioned.
        left (int): The starting index of the subarray.
        right (int): The ending index of the subarray.
        pivot_index (int): The index of the pivot element.

    Returns:
        int: The final index where the pivot element ends up after partitioning.
    """
    # Step 1: Move the pivot to the rightmost position
    # Swap the pivot with the rightmost element
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # Step 2: Iterate through the subarray except the pivot
    # Put the pivot to the end
    ##. Move all elements smaller than the pivot to the left
    final_index = left
    for i in range(left, right):
        # If the current element is smaller than the pivot
        if arr[i] < arr[right]:
            # Swap the current element with the element at the final_index
            arr[final_index], arr[i] = arr[i], arr[final_index]
            # Increment the final index to expand the "smaller than pivot" range
            final_index += 1

    # Step 3: Swap the pivot back to its final position
    # The final place is the 'final index',
    # which is now postiioned just after the elements smaller than the pivot.
    arr[right], arr[final_index] = arr[final_index], arr[right]

    # Return the final index of the pivot
    return final_index

# --- Test Case ---
if __name__ == "__main__":
    # Sample Input list
    # Sorted: [1, 7, 9, 12, 21, 50]
    sample_arr = [12, 7, 9, 1, 21, 50]
    n = len(sample_arr)
    print(f"Sample Array: {sample_arr}")
    print(f"Length of array (n): {n}")
    print("-" * 20)

    # Test Case 1: Find the minimum element (0-th smallest, k=0)
    k_min = 0
    min_element = quick_select(sample_arr, k_min)
    print(f"Finding the element at 0-based index k = {k_min}")
    print(f"The {k_min+1}-st smallest (minimum) element is: {min_element}")
    print(f"(Original array after quick_select: {sample_arr} - Note: quick_select modifies a copy)") # Show original is unchanged
    print("-" * 20)


    # Test Case 2: Find the median element
    # For n=6, the median can be considered the floor(n/2)=3rd element (index 2) or ceil(n/2)=4th element (index 3)
    # Let's find the element at index k=2 (the 3rd smallest)
    # Sorted: [1, 7, 9, 12, 21, 50] -> Element at index 2 is 9
    k_median_lower = (n - 1) // 2 # Index for lower median if n is even
    median_element_lower = quick_select(sample_arr, k_median_lower)
    print(f"Finding the element at 0-based index k = {k_median_lower}")
    print(f"The {k_median_lower+1}-rd smallest (lower median) element is: {median_element_lower}")
    print("-" * 20)

    # Test Case 3: Find the maximum element ((n-1)-th smallest, k=n-1)
    # Sorted: [1, 7, 9, 12, 21, 50] -> Element at index 5 is 50
    k_max = n - 1
    max_element = quick_select(sample_arr, k_max)
    print(f"Finding the element at 0-based index k = {k_max}")
    print(f"The {k_max+1}-th smallest (maximum) element is: {max_element}")
    print("-" * 20)

    # Test Case 4: Another example
    arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 7] # n=13
    # Sorted: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    k_mid = len(arr2) // 2 # k = 6 (7th element) -> Should be 5
    print(f"Second Sample Array: {arr2}")
    result2 = quick_select(arr2, k_mid)
    print(f"Finding the element at 0-based index k = {k_mid}")
    print(f"The {k_mid+1}-th smallest element is: {result2}") # Should be 5
    print("-" * 20)

    # Test Case 5: Edge case - Small array
    arr3 = [5, 2]
    k_small = 0
    print(f"Small Array: {arr3}")
    result3 = quick_select(arr3, k_small)
    print(f"Finding the element at 0-based index k = {k_small}")
    print(f"The {k_small+1}-st smallest element is: {result3}") # Should be 2
    print("-" * 20)
