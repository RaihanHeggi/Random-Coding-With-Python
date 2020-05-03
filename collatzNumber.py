def checkNumber(n):
    if(n%2 == 0):
        collatz = n/2
    else :
        collatz = 3*n+1    
    return collatz

def main():
    n = 30
    i = 1
    cek = True
    while(cek):
        collatzNumber = checkNumber(n)
        print(i," Collatz Number = ",collatzNumber)
        n = collatzNumber
        if(n <=  1):
            cek = False
        i+= 1


if __name__ == "__main__":
    main()