
unique_array = [0, 0, 0.55, 0, 0]

def find_uniq(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        if(a == arr[i]):
            t=0
        else:
            return arr[i]
    return a

print(find_uniq(unique_array))
