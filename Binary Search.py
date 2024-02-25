import random
import time

def naive_search(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1

def binary_search(lst, target):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = lst[mid]

        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            low = mid + 1  # Adjust the search range to the right half
        else:
            high = mid - 1  # Adjust the search range to the left half

    return -1  # Target not found in the list

if __name__ == '__main__':
    user_input = input("Enter a sorted list of numbers separated by spaces: ")
    user_list = list(map(int, user_input.split()))

    target = int(input("Enter the number to search for: "))

    user_list.sort()

    print("User's list:", user_list)
    print("Target:", target)

    start = time.perf_counter()
    naive_result = naive_search(user_list, target)
    end = time.perf_counter()
    naive_time = end - start

    start = time.perf_counter()
    binary_result = binary_search(user_list, target)
    end = time.perf_counter()
    binary_time = end - start

    print("Naive search result:", naive_result)
    print("Binary search result:", binary_result)

    if naive_result != -1:
        print("Naive search found the target at index:", naive_result)
    else:
        print("Naive search did not find the target.")

    if binary_result != -1:
        print("Binary search found the target at index:", binary_result)
    else:
        print("Binary search did not find the target.")

    print("Naive search time:", naive_time, "seconds.")
    print("Binary search time:", binary_time, "seconds.")
