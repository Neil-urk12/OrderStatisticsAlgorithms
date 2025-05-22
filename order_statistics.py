from quickSelect import quick_select

def find_kth_largest(arr, k):
  """
  Finds the k-th largest element in a list of numbers.

  Args:
    arr: A list of numbers.
    k: An integer representing the k-th largest element to find (1-based).

  Returns:
    The k-th largest element in the list.

  Raises:
    ValueError: If k is less than or equal to 0, or greater than the length of the array,
                or if the input array is empty.
  """
  n = len(arr)
  if not arr:
    raise ValueError("Input array cannot be empty.")
  if k <= 0 or k > n:
    raise ValueError(f"k must be between 1 and {n} (inclusive), but got {k}.")

  # Convert 1-based k-th largest to 0-based k-th smallest for quick_select
  # The k-th largest element is at index n-k when sorted.
  # quick_select is 0-indexed, so we pass n-k.
  kth_smallest_index = n - k
  return quick_select(arr, kth_smallest_index)

def find_min_max(arr):
  """
  Finds the minimum and maximum elements in a list of numbers using pairwise comparisons.
  This method aims for approximately 3n/2 comparisons.

  Args:
    arr: A list of numbers.

  Returns:
    A tuple (min_val, max_val) containing the minimum and maximum values in the list.

  Raises:
    ValueError: If the input array is empty.
  """
  n = len(arr)
  if not arr:
    raise ValueError("Input array cannot be empty.")

  # Initialize min_val and max_val
  if n % 2 == 1: # Odd number of elements
    min_val = arr[0]
    max_val = arr[0]
    start_index = 1
  else: # Even number of elements
    if arr[0] < arr[1]:
      min_val = arr[0]
      max_val = arr[1]
    else:
      min_val = arr[1]
      max_val = arr[0]
    start_index = 2

  # Process elements in pairs
  for i in range(start_index, n - 1, 2):
    # Compare the pair
    if arr[i] < arr[i+1]:
      current_min = arr[i]
      current_max = arr[i+1]
    else:
      current_min = arr[i+1]
      current_max = arr[i]
    
    # Update overall min and max
    if current_min < min_val:
      min_val = current_min
    if current_max > max_val:
      max_val = current_max
      
  return (min_val, max_val)

if __name__ == "__main__":
  print("--- Testing find_kth_largest ---")
  data = [3, 1, 4, 1, 5, 9, 2, 6] # sorted: [1, 1, 2, 3, 4, 5, 6, 9]
  k_value = 3 # 3rd largest should be 5
  try:
    kth_largest_element = find_kth_largest(list(data), k_value) # Pass a copy as quick_select might modify
    print(f"The {k_value}-rd largest element in {data} is: {kth_largest_element}")
  except ValueError as e:
    print(e)

  data_2 = [10, 4, 5, 8, 6, 11, 26] # sorted: [4, 5, 6, 8, 10, 11, 26]
  k_value_2 = 1 # 1st largest should be 26
  try:
    kth_largest_element_2 = find_kth_largest(list(data_2), k_value_2)
    print(f"The {k_value_2}-st largest element in {data_2} is: {kth_largest_element_2}")
  except ValueError as e:
    print(e)

  data_3 = [1, 2, 3, 4, 5] # sorted: [1, 2, 3, 4, 5]
  k_value_3 = 5 # 5th largest should be 1
  try:
    kth_largest_element_3 = find_kth_largest(list(data_3), k_value_3)
    print(f"The {k_value_3}-th largest element in {data_3} is: {kth_largest_element_3}")
  except ValueError as e:
    print(e)
  
  # Edge case: k > len(arr)
  data_4 = [1, 2, 3]
  k_value_4 = 4
  try:
    kth_largest_element_4 = find_kth_largest(list(data_4), k_value_4)
    print(f"The {k_value_4}-th largest element in {data_4} is: {kth_largest_element_4}")
  except ValueError as e:
    print(f"Error for find_kth_largest data_4 ({data_4}), k_value_4 ({k_value_4}): {e}")

  # Edge case: k <= 0
  data_5 = [1, 2, 3]
  k_value_5 = 0
  try:
    kth_largest_element_5 = find_kth_largest(list(data_5), k_value_5)
    print(f"The {k_value_5}-th largest element in {data_5} is: {kth_largest_element_5}")
  except ValueError as e:
    print(f"Error for find_kth_largest data_5 ({data_5}), k_value_5 ({k_value_5}): {e}")

  # Empty array case for find_kth_largest
  data_6 = []
  k_value_6 = 1
  try:
    kth_largest_element_6 = find_kth_largest(list(data_6), k_value_6)
    print(f"The {k_value_6}-th largest element in {data_6} is: {kth_largest_element_6}")
  except ValueError as e:
    print(f"Error for find_kth_largest data_6 ({data_6}), k_value_6 ({k_value_6}): {e}")

  # Array with one element for find_kth_largest
  data_7 = [42]
  k_value_7 = 1
  try:
    kth_largest_element_7 = find_kth_largest(list(data_7), k_value_7)
    print(f"The {k_value_7}-st largest element in {data_7} is: {kth_largest_element_7}")
  except ValueError as e:
    print(f"Error for find_kth_largest data_7 ({data_7}), k_value_7 ({k_value_7}): {e}")
  
  # Array with duplicate elements for find_kth_largest
  data_8 = [3, 3, 3, 3]
  k_value_8 = 2 # 2nd largest should be 3
  try:
    kth_largest_element_8 = find_kth_largest(list(data_8), k_value_8)
    print(f"The {k_value_8}-nd largest element in {data_8} is: {kth_largest_element_8}")
  except ValueError as e:
    print(f"Error for find_kth_largest data_8 ({data_8}), k_value_8 ({k_value_8}): {e}")

  print("\n--- Testing find_min_max ---")
  # Test case 1: Empty list
  test_arr_1 = []
  try:
    min_val, max_val = find_min_max(test_arr_1)
    print(f"Array: {test_arr_1}, Min: {min_val}, Max: {max_val}")
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_1}: {e}")

  # Test case 2: List with one element
  test_arr_2 = [5]
  try:
    min_val, max_val = find_min_max(test_arr_2)
    print(f"Array: {test_arr_2}, Min: {min_val}, Max: {max_val}") # Expected: Min: 5, Max: 5
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_2}: {e}")

  # Test case 3: List with even number of elements
  test_arr_3 = [3, 1, 4, 1, 5, 9, 2, 6]
  try:
    min_val, max_val = find_min_max(test_arr_3)
    print(f"Array: {test_arr_3}, Min: {min_val}, Max: {max_val}") # Expected: Min: 1, Max: 9
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_3}: {e}")

  # Test case 4: List with odd number of elements
  test_arr_4 = [3, 1, 4, 1, 5, 9, 2]
  try:
    min_val, max_val = find_min_max(test_arr_4)
    print(f"Array: {test_arr_4}, Min: {min_val}, Max: {max_val}") # Expected: Min: 1, Max: 9
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_4}: {e}")

  # Test case 5: List with negative numbers
  test_arr_5 = [-10, -2, -5, -1, -20]
  try:
    min_val, max_val = find_min_max(test_arr_5)
    print(f"Array: {test_arr_5}, Min: {min_val}, Max: {max_val}") # Expected: Min: -20, Max: -1
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_5}: {e}")

  # Test case 6: List with duplicate numbers
  test_arr_6 = [5, 5, 5, 5, 5]
  try:
    min_val, max_val = find_min_max(test_arr_6)
    print(f"Array: {test_arr_6}, Min: {min_val}, Max: {max_val}") # Expected: Min: 5, Max: 5
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_6}: {e}")
    
  # Test case 7: Mixed positive and negative
  test_arr_7 = [-5, 10, 0, -2, 8]
  try:
    min_val, max_val = find_min_max(test_arr_7)
    print(f"Array: {test_arr_7}, Min: {min_val}, Max: {max_val}") # Expected: Min: -5, Max: 10
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_7}: {e}")

  # Test case 8: Two elements, first smaller
  test_arr_8 = [2, 7]
  try:
    min_val, max_val = find_min_max(test_arr_8)
    print(f"Array: {test_arr_8}, Min: {min_val}, Max: {max_val}") # Expected: Min: 2, Max: 7
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_8}: {e}")

  # Test case 9: Two elements, first larger
  test_arr_9 = [7, 2]
  try:
    min_val, max_val = find_min_max(test_arr_9)
    print(f"Array: {test_arr_9}, Min: {min_val}, Max: {max_val}") # Expected: Min: 2, Max: 7
  except ValueError as e:
    print(f"Error for find_min_max {test_arr_9}: {e}")
