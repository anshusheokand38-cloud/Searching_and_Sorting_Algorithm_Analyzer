import time

# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Main Program
print("SEARCHING AND SORTING ALGORITHM ANALYZER")

data = list(map(int, input("Enter numbers separated by space: ").split()))

print("\nOriginal List:")
print(data)

print("\n1. Searching")
print("2. Sorting")

choice = int(input("Enter your choice: "))

if choice == 1:

    key = int(input("Enter element to search: "))

    print("\n1. Linear Search")
    print("2. Binary Search")

    search_choice = int(input("Choose searching algorithm: "))

    if search_choice == 1:
        start = time.perf_counter()
        result = linear_search(data, key)
        end = time.perf_counter()

        if result != -1:
            print("Element found at index:", result)
        else:
            print("Element not found")

        print("Execution Time:",
              end - start, "seconds")

    elif search_choice == 2:
        sorted_data = sorted(data)

        start = time.perf_counter()
        result = binary_search(sorted_data, key)
        end = time.perf_counter()

        print("Sorted List:", sorted_data)

        if result != -1:
            print("Element found at index:", result)
        else:
            print("Element not found")

        print("Execution Time:",
              end - start, "seconds")

elif choice == 2:

    print("\n1. Bubble Sort")
    print("2. Quick Sort")
    print("3. Merge Sort")

    sort_choice = int(input("Choose sorting algorithm: "))

    if sort_choice == 1:
        start = time.perf_counter()
        result = bubble_sort(data.copy())
        end = time.perf_counter()

        print("Sorted List:", result)
        print("Execution Time:",
              end - start, "seconds")

    elif sort_choice == 2:
        start = time.perf_counter()
        result = quick_sort(data)
        end = time.perf_counter()

        print("Sorted List:", result)
        print("Execution Time:",
              end - start, "seconds")

    elif sort_choice == 3:
        start = time.perf_counter()
        result = merge_sort(data)
        end = time.perf_counter()

        print("Sorted List:", result)
        print("Execution Time:",
              end - start, "seconds")

    else:
        print("Invalid sorting choice.")

else:
    print("Invalid choice.")