"""
Time Complexity:
    - Best Case: O(n)
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

Space Complexity:
    - O(1)
"""

def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = list(map(int, user_input.split()))
    print("Original Array:", sample_data)
    sorted_data = bubble_sort(sample_data.copy())
    print("Sorted Array (Bubble Sort):", sorted_data)


if __name__ == "__main__":
    main()
