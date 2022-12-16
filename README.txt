```python
def linear_search(haystack, needle):
    for index in range(0, len(haystack)):
        if haystack[index] == needle:
            return True
        return False
# Go 1 by 1 until you find a match, if you find one simply return True
```

```python
from math import floor

haystack=[]
for i in range(0,348256):
    haystack.append(i)

def binary_search(haystack, needle):
    lo = 0
    # minimal value
    hi = len(haystack)
    # max value

    while lo < hi:
        midPoint = floor(lo + (hi - lo) / 2)
        print(midPoint)
        # get midpoint value
        v = haystack[int(midPoint)]
        # get middle value
        if v == needle:
            return True
            # If we got it, return True
        elif v > needle:
            hi = midPoint
            # If our value is bigger than out midPoint we only use the first half
        else:
            lo = midPoint + 1
            # If our value is smaller than our midPoint our min point becomes midpoint+1
    return False

binary_search(haystack, 128300)
```

```python
from math import floor,sqrt

breakPoints = [False, False, False, False, False, False, False, False, False, False, True, True, True, True, ]


def two_crystal_balls(breaks):
    jmpAmount = floor(sqrt(len(breaks)))
    # Define the jump amount as the square root of break's len
    index = jmpAmount
    print(index)
    # Set it as index
    for _ in range(len(breaks)):
        if breaks[index]:
            print(index)
            break
            # If we find a true we break
        index += jmpAmount
        # If we don't find a true we keep adding

    index -= jmpAmount
    # We found a true, so now we have to go back to a safe position
    # From this safe position we will lineary search

    for _ in range(len(breaks)):
        if (breaks[index]):
            return index
        index += 1
        print(index)
        # We add to the index until we find the first true position

    return False

two_crystal_balls(breakPoints)
```

```python
from random import randint
unsortedArray=[]
for i in range(50):
    unsortedArray.append(randint(0,100))

def bubble_sort(array):
    for index in range(len(array)):
        # For each element in the array:
        for j in range(len(array)-1-index):
            #For each elemnt in the array:
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                # If the number in front is bigger we swap values

bubble_sort(unsortedArray)
print(unsortedArray)
```
