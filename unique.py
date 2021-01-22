unique_array = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]

def find_uniq(arr):
    for i in range(1,len(arr)):
        if(arr[0] == arr[i]):
            t=0
        elif((i == 1) and (arr[i] == arr[i+1])):
            return arr[0]
        else:
            return arr[i]
    

print(find_uniq(unique_array))
