def ispalindrome(word):
    if len(word)<1:
        return True
    else:
        if word[0]==word[-1]:
            return ispalindrome(word[i:-1])
        else:
            return False
def fileinput(filename):
    palindromes=False
    fh=open(filename,"r")
    length=input("enter length of palindromes: ")
    d=int(length)
    try:
        for line in fn:
            for s in str(len(line)):
                if ispalindrome(line.strip()):
                    palindromes=True
                    if(len(line.strip())==d):
                        print(line.strip())
    except:
        print("no palindromes found for length entered")
    finally:
        fh.close()