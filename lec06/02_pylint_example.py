'''Diese ist eine Beispiel Datei um pylint zu demonstrieren.'''

import numpy as np

def quicksort(arr):
    '''sortiert einen array iterativ'''
    print('Ich werde gerade aufgerufen.')
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
