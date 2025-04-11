import random #For random selecting of pivot
"""
 Find the k-th smallest element in the array using Quick Select.

 The parameter nums, is a list of unsorted elements.
 The parameter k determines which smallest element to find

 Returns:
 - The k-th smallest element in the array.

 Raises:
 - ValueError or IndexError if k is out of bounds.
"""
    
# -> int, this means that this function returns an integer
def quick_select(arr: list[int], k: int) -> int: # I explicitly stated the data types
    if k < 0 or k >= len(arr):
        raise ValueError("k is out of bounds")
    
    # Call the helper function to start the Quick Select process
    # The helper function handles the selecting of random pivots
    return pivot_selector(arr, k, 0, len(arr) - 1)

def pivot_selector(arr, k, left, right):
    # If the list contains only one element, return that element
    if left == right:
        return arr[left]

    # Select a random pivot index
    pivot_index = random.randint(left, right)

    # Partition the array around the pivot
    pivot_index = partition(arr, left, right, pivot_index)

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
    # Swap the pivot with the rightmost element
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # Initialize the store index
    store_index = left

    # Move all elements smaller than the pivot to the left
    for i in range(left, right):
        if arr[i] < arr[right]:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Swap the pivot back to its final position
    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index

if __name__ == "__main__":
    arr = [12, 7, 9, 1, 21, 50]
    k = 0 
    result = quick_select(arr, k)
    print(f"The {k}-th smallest element is: {result}")
