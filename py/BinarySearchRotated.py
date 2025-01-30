def binary_search_rotated(arr, target, rotation_index):
    """
    Perform binary search on a rotated sorted array.
    
    A rotated sorted array is an array that was initially sorted in ascending order
    but then rotated at a certain pivot index.
    
    Example:
    Original sorted array: [0, 1, 2, 4, 5, 6, 7]
    Rotated at index 4: [4, 5, 6, 7, 0, 1, 2]
    Here, the rotation index 4 means that the first four elements were moved to the end.
    
    :param arr: List[int] - The rotated sorted array.
    :param target: int - The number to search for.
    :param rotation_index: int - The index at which the array was rotated.
    :return: bool - True if the target is in the array, False otherwise.
    """
    
    # TODO: Check if the rotation_index is 0, meaning the array is not rotated.
    
    # TODO: Determine which half (before or after rotation_index) the target belongs to.

    n = len(arr)
    
    if n == 0:
        return False
    
    if rotation_index == 0:
        # Array is not rotated; perform standard binary search
        left, right = 0, n - 1
    elif target >= arr[rotation_index] and target <= arr[n - 1]:
        # Target is in the rotated half
        left, right = rotation_index, n - 1
    else:
        # Target is in the non-rotated half
        left, right = 0, rotation_index - 1
    
    def binary_search(arr, left, right, target):
        """Performs binary search on a sorted subarray."""
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    return binary_search(arr, left, right, target)