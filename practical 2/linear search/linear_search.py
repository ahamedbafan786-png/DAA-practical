"""
Time Complexity:
    - Best Case: O(1)
    - Average Case: O(n)
    - Worst Case: O(n)

Space Complexity:
    - O(1)
"""

def linear_search(arr: list, target: int) -> int:
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


def main():
    user_input = input("Enter numbers separated by spaces: ")
    sample_list = list(map(int, user_input.split()))
    target_val = int(input("Enter element to search for: "))

    print("Array:", sample_list)
    print(f"Searching for target: {target_val}")
    result = linear_search(sample_list, target_val)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")


if __name__ == "__main__":
    main()
