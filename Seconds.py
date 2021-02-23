def make_readable(seconds):
    h = seconds // 3600
    seconds -= (3600 * h)
    m = seconds // 60
    seconds -= (60 * m)
    s = seconds 
    seconds -= (s)
    r = ""
    if(h < 10):
        r += "0"
    r += str(h)
    r += ":"
    if(m < 10):
        r += "0"
    r += str(m)
    r += ":"
    if(s < 10):
        r += "0"
    r += str(s)
    return r

a = 86399

print(make_readable(a))