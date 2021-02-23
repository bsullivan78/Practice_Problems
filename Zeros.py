def move_zeros(array):
    na = []
    for a in array:
        if a != 0 : 
            na.append(a)
    while((len(na)) < (len(array))):
        na.append(0)
    return na



arr = []
print(arr)
print(move_zeros(arr))