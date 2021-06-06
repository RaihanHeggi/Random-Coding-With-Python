# Buatlah Program dimana menghitung berapa banyak langkah yang dapat dilakukan
# Ketika menyelesaikan permasalahan Tower of Hanoi Hint (2^k-1)

import math


def hitungMove(disks):
    return math.pow(2, disks) - 1


def main():
    trueValue = [1, 3, 7, 31, 1023, 1048575]
    stringTest = [1, 2, 3, 5, 10, 20]
    functionValue = []
    for x in stringTest:
        functionValue.append(hitungMove(x))
    if trueValue == functionValue:
        print("Program Benar")
        print(str(functionValue))
    else:
        print("Program Salah")
        print(str(functionValue))


if __name__ == "__main__":
    main()

