#finding the square root
def floor_root(x):
    if (x==0) & (x==1):
        return x
    i = 1
    result = 1
    while (result<=x):
        i+=1
        result = i*i
    return i-1
x = 11
print(floor_root(x))
