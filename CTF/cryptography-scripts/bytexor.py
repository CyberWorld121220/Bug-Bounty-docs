from itertools import cycle

def bytexor(data, key):
    return bytes([i^j for i,j in zip(data,cycle(key))])

