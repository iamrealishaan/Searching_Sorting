# to find first occurence and last occurnece
def first_occurence(arr , x):
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid] == x:
            result = mid
            right = mid-1
        elif arr[mid]<x:
            left = mid+1
        else:
            right = mid-1
    return result

def last_occurence(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result =  mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result
# Testing the function
sorted_arr = [1,3,5,5,5,5,7,9]
x = 5
f_o = first_occurence(sorted_arr, x)
l_o = last_occurence(sorted_arr, x )
print("First Ocuurence is :", f_o)
print("Last Occurence is:", l_o)
