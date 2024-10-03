
if __name__ == "__main__":
    x, op, y = input().split()
    x = int(x)
    y = int(y)

    if(op == '+'):
        print(f"{x} + {y} = {x + y}")
    elif(op == '*'):
        print(f"{x} * {y} = {x * y}")
    elif(op == '-'):
        print(f"{x} - {y} = {x - y}")
    else:
        print("Format incorect!")
    