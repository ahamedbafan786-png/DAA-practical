"""
Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity:
    - O(1)
"""

def heapify(arr: list, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def main():
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = list(map(int, user_input.split()))
    print("Original Array:", sample_data)
    sorted_data = heap_sort(sample_data.copy())
    print("Sorted Array (Heap Sort):", sorted_data)


if __name__ == "__main__":
    main()
