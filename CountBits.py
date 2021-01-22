def count_bits(n):
    bi = format(n, "b")
    n = 0
    for i in bi:
        if(i == '1'):
            n += 1
    return n

print(count_bits(1234)) #place number to count bits here
