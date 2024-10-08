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


if __name__ == "__main__":
    v = [3, 1, 5, 2, 7, 8]
    print(odd_prod(v))

