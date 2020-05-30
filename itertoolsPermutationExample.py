from itertools import permutations

def main():
    s = str(input())
    splitValue = s.split()
    listHasil = list(permutations(sorted(splitValue[0]),int(splitValue[1])))
    for i in range(len(listHasil)):
        hasil = ''.join(listHasil[i])
        print(hasil)

if __name__ == "__main__":
    main()