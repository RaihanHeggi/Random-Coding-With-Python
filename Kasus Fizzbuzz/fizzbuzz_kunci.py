def fizzbuzz(x):
    temp = ""
    if x % 3 == 0:
        if x % 5 == 0:
            temp = "FizzBuzz"
        else:
            temp = "Fizz"
    elif x % 5 == 0:
        temp = "Buzz"
    else:
        temp = str(x)
    return temp


def main():
    hasil = []
    for i in range(1, 21):
        hasil.append(fizzbuzz(i))
    print(hasil)


if __name__ == "__main__":
    main()

