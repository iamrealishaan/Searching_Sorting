#Find a Fixed Point (Value equal to index) in a given array
def find_number(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1
arr = [1,2,5,3,9]
result = find_number(arr)
print(result)
