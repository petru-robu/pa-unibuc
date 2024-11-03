
if __name__ == "__main__":

    sir =  input()
    words = sir.split()

    lgmax = -1

    i=0
    while i < len(words):
        seq = []
        while i < len(words)-1 and words[i][-1] == words[i+1][0]:
            seq.append(words[i])
            i+=1

        if i < len(words)
            seq.append(words[i])
        
        if len(seq) > lgmax:
            lgmax = len(seq)
            
        i+=1
