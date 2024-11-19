    
def in_list(x, *l):
    ans = []
    for list in l:
        if x in list:
            ans.append(list)
    return ans

if __name__ == '__main__':

    l1 = [1, 2, 3]
    l2 = [1, 4, 5]
    l3 = [1, 7, 3]

    print(in_list(3, l1, l2, l3))