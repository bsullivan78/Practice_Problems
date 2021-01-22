
unique_array = [0, 0, 0.55, 0, 0] #array of numbers goes here

def find_uniq(arr):
    for i in range(1,len(arr)):
        if(arr[0] == arr[i]):
            t=0
        else:
            return arr[i]
    return arr[0]

print(find_uniq(unique_array))
