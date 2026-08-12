"""
Time Complexity:
    - Best Case: O(n^2)
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

Space Complexity:
    - O(1)
"""

def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = list(map(int, user_input.split()))
    print("Original Array:", sample_data)
    sorted_data = selection_sort(sample_data.copy())
    print("Sorted Array (Selection Sort):", sorted_data)


if __name__ == "__main__":
    main()
