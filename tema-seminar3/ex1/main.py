def anagrams(s1, s2):
    map = {}
    for ch in s1:
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] += 1
    for ch in s2:
        if ch not in map:
            return False
        else:
            map[ch] -= 1

    for key in map:
        if map[key] != 0:
            return False
        
    return True


if __name__ == '__main__':
    s1 = 'emerit'
    s2 = 'treime'
    print(anagrams(s1, s2))