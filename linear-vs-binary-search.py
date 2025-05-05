import random
import time


def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]


def choose_random_number(array):
    random_index = random.randint(0, len(array) - 1)
    return array[random_index]


def linear_search(array, target):
    for x in range(len(array)):
        if array[x] == target:
            return x


def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


size = 100000
array = generate_random_array(size)
sorted_array = sorted(array)
target = choose_random_number(sorted_array)

print("--- Linear Search ---")
start_time = time.time()
result = linear_search(sorted_array, target)
print("Target: %s, Index: %s" % (target, result))
print("--- %s seconds ---" % (time.time() - start_time))

print("--- Binary Search ---")
start_time = time.time()
result = binary_search(sorted_array, target)
print("Target: %s, Index: %s" % (target, result))
print("--- %s seconds ---" % (time.time() - start_time))

