
if __name__ == "__main__":
    
    
    while True:
        try:
            line = input()
            print(line[::-1])
        except EOFError:
            print("Eroare EOF!")
            exit(0)