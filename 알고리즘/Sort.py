original = [13, 42, 7, 19, 3, 25, 8, 31, 16, 4]

# Bubble Sort 

arr = original.copy()

for i in range(len(arr) - 1):
    swapped = False

    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

print(arr)
        
# Selection Sort 

arr = original.copy()

for i in range(len(arr) - 1):
    min_idx = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
            
# Insertion Sort 

arr = original.copy()

for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    
    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = temp

print(arr)
