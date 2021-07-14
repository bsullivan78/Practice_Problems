import math
def start(h, d, vt):
    r = d/2
    vol = (vt / (math.pi * (r * r))) * ((r * r) * math.acos((r - h) / r) - (r - h) * math.sqrt(2 * r * h - (h * h)))
    return int(vol)

#--main--
print(start(40, 120, 3500))
print(start(60,120,3500))