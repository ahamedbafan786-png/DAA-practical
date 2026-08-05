"""
Linear Search Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(1) when target is at the first position
    - Average Case: O(n)
    - Worst Case: O(n) when target is at the end or not present

Space Complexity:
    - O(1) Auxiliary Space
"""

def linear_search(arr: list, target: int) -> int:

    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


if __name__ == "__main__":
    sample_list = [10, 50, 30, 70, 80, 20, 90, 40]
    target_val = 30

    print("Array:", sample_list)
    print(f"Searching for target: {target_val}")
    result = linear_search(sample_list, target_val)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")

    missing_val = 100
    print(f"\nSearching for missing target: {missing_val}")
    result_missing = linear_search(sample_list, missing_val)
    print(f"Result: {result_missing}")
