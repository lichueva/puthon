import math

def calculate_z(x):
    if x >= 1:
        print("x повинно бути менше 1")
        return
    z = math.exp(math.sqrt(x)) / math.sqrt(1 - x)
    return z
