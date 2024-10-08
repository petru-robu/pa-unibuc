from random import randrange

def choice(data):
    ind = randrange(0, len(data))
    return data[ind]


def odd_prod(data):
    for x in data:
        for y in data:
            if x != y and x * y % 2 == 1:
                return (x, y)
    return None

def diff(data):
    ap = set()
    for x in data:
        if x in ap:
            return False
        else:
            ap.add(x)

    print(ap)
    return True
    
        
if __name__ == "__main__":
    v = [3, 1, 5, 2, 0, 8]

    #l = [x*(x+1) for x in range(1, 10)]

    l = [chr(x) for x in range(ord('a'), ord('z')+1)]
    print(l)

