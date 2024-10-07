
def minmax(data):
    min  = max = data[0]
    for el in data:
        if el < min:
            min = el
        if el > max:
            max = el
    return (min, max)

if __name__ == "__main__":
    list = [12, 3, 4, 6, -121, 34, 5, 9, -3, -21]
    print(minmax(list))