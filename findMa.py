def checkMax(a,b,c):
    max = 0
    if((a>b) and (a>c)):
        max = a 
    elif((b>a) and (b>c)):
        max = b
    else :
        max = c 
    return max

def main():
    a = int(input("Masukkan Nilai : "))
    b = int(input("Masukkan Nilai : "))
    c = int(input("Masukkan Nilai : "))
    maximumValue = checkMax(a,b,c)
    print(maximumValue)
    print(max(a,b,c))

if __name__ == "__main__":
    main()