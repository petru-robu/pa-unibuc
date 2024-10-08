
if __name__ == "__main__":
    
    l = [1, 2, 7]
    try:
        l[2] = 5
        print(l)
    except IndexError:
        print("Out of bounds!")