if __name__ == '__main__':
    fin = open("exemplu.txt", "r")
    fout = open("grupe_cuvinte.txt", "w")

    map = {}

    for line in fin:
        for word in line.split():
            word = ''.join(ch for ch in word if ch.isalnum())
            word = word.lower()

            if len(word) not in map:
                map[len(word)] = set()

            map[len(word)].add(word)


    for key in sorted(map, reverse=True):
        print(f'Lungime {key}: {', '.join(sorted(map[key]))}', file=fout)