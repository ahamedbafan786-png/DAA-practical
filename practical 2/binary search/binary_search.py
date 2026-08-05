"""
Time Complexity:
    - Best Case: O(1)
    - Average Case: O(log n)
    - Worst Case: O(log n)

Space Complexity:
    - Iterative: O(1)
    - Recursive: O(log n)
"""

def binary_search_iterative(arr: list, target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr: list, target: int, low: int, high: int) -> int:
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)

    return -1


if __name__ == "__main__":
    user_input = input("Enter sorted numbers separated by spaces: ")
    sorted_array = list(map(int, user_input.split()))
    target_val = int(input("Enter element to search for: "))

    print("Sorted Array:", sorted_array)
    print(f"Target value: {target_val}")

    res_iterative = binary_search_iterative(sorted_array, target_val)
    print(f"Iterative Binary Search result index: {res_iterative}")

    res_recursive = binary_search_recursive(sorted_array, target_val, 0, len(sorted_array) - 1)
    print(f"Recursive Binary Search result index: {res_recursive}")
