import os

def absoluteNumber(x):
    absX = 0
    if(x>=0):
        absX = x
    else :
        absX = -x
    print(absX)
    pilihan = str(input('Ingin Kembali Memasukkan Angka (Y/N): '))
    if(pilihan == "Y"):
        main()
    else : 
        print("End Of Program")

def main():
    x = int(input("Silahkan Masukan Angka : "))
    absoluteNumber(x)
    os.system('cls')

if __name__ == "__main__":
    main()
