def func1(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;
        
def func2(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;

def func3(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def func4(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 
     
def func5(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;
    
if __name__ == '__main__':
    s = input()
    alphanum = func1(s)
    alphabetical = func2(s)
    digits = func3(s)
    lowercase = func4(s)
    uppercase = func5(s)
    print(alphanum)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
