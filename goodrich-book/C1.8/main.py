
if __name__ == "__main__":
    s = "Let's try, Mike!"
    ans = ""

    for i in range(len(s)):
        if(s[i].isalpha() or 
            s[i].isdigit() or s[i] == ' '):
            ans += s[i]

    print(ans)
            
