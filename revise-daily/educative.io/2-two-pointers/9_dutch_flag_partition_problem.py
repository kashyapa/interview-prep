import math


def dutch_national_flag(arr, pivot):
    smaller, equal, larger = 0, 0, len(arr) - 1

    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] > pivot:
            arr[larger], arr[equal] = arr[equal], arr[larger]
            larger -= 1
        else:
            equal += 1
    return arr

