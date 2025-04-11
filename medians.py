import math

def find_median_of_group(arr):
  """
  Finds the median of a small group (<= 5 elements) by sorting.
  Args:
    arr: A list of numbers (ideally size 5 or less).
  Returns:
    The median element of the arr.
  """
  arr.sort()
  # Find the middle index (integer division)
  median_index = len(arr) // 2
  return arr[median_index]

def median_of_medians(arr, k):
  """
  Finds the k-th smallest element in the list 'arr' using the Median of Medians algorithm.

  Args:
    arr: The list of numbers.
    k: The 0-based index of the element to find (e.g., 0 for minimum, len(arr)//2 for median).

  Returns:
    The k-th smallest element in arr.
  """
  n = len(arr)

  # Base case: If the list is small, sort and return the k-th element
  if n <= 5:
    arr.sort()
    # Check if k is within bounds for the small list
    if 0 <= k < n:
        return arr[k]
        # It's okay to use return sorted(arr)[k] too
    else:
        # Handle cases where k might be invalid after recursion (should ideally not happen)
        raise IndexError("k is out of bounds for the small list")

  # Step 1: Divide arr into groups of 5
  # Two ways of calculating the number of chunks/sublists
  # num_chunks = math.ceil(n / 5) + chunks = [arr[i * 5:(i + 1) * 5] for i in range(num_chunks)]
  chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]

  # Step 2: Find the median of each chunk
  medians = [find_median_of_group(chunk) for chunk in chunks]

  # Step 3: Recursively find the median of the medians or the pivot
  # The index for the median of medians is the middle index of the 'medians' list
  pivot_index_in_medians = len(medians) // 2
  # Can be simplified to `pivot = median_of_medians(medians, len(medians)//2)`
  pivot = median_of_medians(medians, pivot_index_in_medians)

  # Step 4: Partition the original array 'arr' around the pivot
  low = [x for x in arr if x < pivot]
  mid = [x for x in arr if x == pivot] # Elements equal to the pivot/median
  high = [x for x in arr if x > pivot]

  len_low = len(low)
  len_mid = len(mid)

  # Step 5: Recurse or return based on k's position relative to partitions
  if k < len_low:
    # k-th element is in the 'low' partition
    return median_of_medians(low, k)
  elif k < len_low + len_mid:
    # k-th element is the pivot itself (or one of the elements equal to it)
    return pivot # Or equivalently mid[0]
  else:
    # k-th element is in the 'high' partition
    # Adjust k because we are discarding 'low' and 'mid' elements
    return median_of_medians(high, k - len_low - len_mid)

# --- Sample Usage ---

# Sample Input List
sample_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 7] # n = 13

# Test cases :

# Find the median element
# For n=13, the median is the element at index floor(n/2) = 6 in the sorted list (0-based index)
# Sorted: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9] -> The 6th element is 5
k_median = len(sample_arr) // 2  # k = 6

median_value = median_of_medians(sample_arr, k_median)
print(f"Sample Array: {sample_arr}")
print(f"Length of array (n): {len(sample_arr)}")
print(f"Finding the element at 0-based index k = {k_median}")
print(f"The median (k={k_median}) is: {median_value}")
print("-" * 20)

# Find the 3rd smallest element (index k=2)
# Sorted: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9] -> The 2nd element (index 2) is 2
k_small = 2
third_smallest = median_of_medians(sample_arr, k_small)
print(f"Finding the element at 0-based index k = {k_small}")
print(f"The {k_small+1}-rd smallest (k={k_small}) is: {third_smallest}")
print("-" * 20)

# Find the largest element (index k=n-1)
k_large = len(sample_arr) - 1
largest = median_of_medians(sample_arr, k_large)
print(f"Finding the element at 0-based index k = {k_large}")
print(f"The largest (k={k_large}) is: {largest}")
print("-" * 20)

# --- Explanation of Sample Run (Finding Median, k=6) ---

# uncomment and remov the indentation to test the trace
#print("\n---Detailed Trace for Finding Median (k=6)---")

# Initial Call: median_of_medians([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 7], 6)
# 1. n = 13. Not <= 5. Proceed.
# 2. Divide into chunks of 5:
#chunks = [[3, 1, 4, 1, 5], [9, 2, 6, 5, 3], [5, 8, 7]]
#print(f"Initial Chunks: {chunks}")
# 3. Find median of each chunk:
#    median([1, 1, 3, 4, 5]) = 3
#    median([2, 3, 5, 6, 9]) = 5
#    median([5, 7, 8]) = 7
#medians = [3, 5, 7]
#print(f"Medians of chunks: {medians}")
# 4. Recursively find median of medians: median_of_medians([3, 5, 7], 1) (since len(medians)//2 = 3//2 = 1)
#    Base case: len([3, 5, 7]) <= 5. Sort: [3, 5, 7]. Return element at index 1, which is 5.
#    Pivot = 5
#print(f"Pivot (Median of Medians): {5}")
# 5. Partition original array [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 7] around pivot 5:
#low = [3, 1, 4, 1, 2, 3] (elements < 5)
#mid = [5, 5, 5]         (elements == 5)
#high = [9, 6, 8, 7]      (elements > 5)
#print(f"Partition: low={low}, mid={mid}, high={high}")
# 6. Check k: We are looking for k=6.
#len(low) = 6
#len(mid) = 3
#    Is k < len(low)? Is 6 < 6? No.
#    Is k < len(low) + len(mid)? Is 6 < 6 + 3? Is 6 < 9? Yes.
#    The k-th element is the pivot itself.
# 7. Return pivot: 5

#print("Final result matches the expected median.")
