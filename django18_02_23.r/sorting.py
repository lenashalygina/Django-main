import random
import time

def f_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = []
        middle = arr[0]
        right = []
        for i in arr[1:]:
            if i < middle:
                left.append(i)
            else:
                right.append(i)
        return f_sort(left) + [middle] + f_sort(right)



def absorb_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        absorb_sort(left)
        absorb_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 100 + 1)]

    time_start = time.perf_counter()
    print("Sorted list: ", sorted(absorb_sort(list1)))
    time_stop = time.perf_counter()


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 1000 + 1)]

    t_start = time.perf_counter()
    print("sorted list: ", sorted(selection_sort(list1)))
    t_stop = time.perf_counter()