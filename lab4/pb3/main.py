
if __name__ == '__main__':
    vocale = 'aeiou'

    print(''.join([x + 'p' + x if x in vocale else x for x in input()]))
