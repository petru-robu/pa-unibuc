if __name__ == '__main__':

    l = [1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 1, 2, 3]

    p = 0
    
    while True:
        try:
            l.remove(0)
        except ValueError:
            print('Lista fara zerouri este: ', l)
            break
        