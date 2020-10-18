# menghitung golden ratio
def goldenRation(fibonacci):
    goldenRatio = []
    for i in range(len(fibonacci) - 1):
        ratio = fibonacci[i + 1] / fibonacci[i]
        goldenRatio.append(ratio)
    return goldenRatio


# menghitung fibonacci
def fibonacci(nilaiMasukan):
    if nilaiMasukan <= 1:
        return 1
    else:
        return fibonacci(nilaiMasukan - 1) + fibonacci(nilaiMasukan - 2)


# main program
def main():
    print("Welcome to Fibonacci Application")
    banyakFibonacci = int(
        input("Silahkan Masukan berapa banyak angka yang akan di generate : ")
    )
    fibo_series = []
    goldenRatio = []
    for i in range(banyakFibonacci):
        fibo_series.append(fibonacci(i))
    goldenRatio = goldenRation(fibo_series)
    print("Barisan Fibonacci : ", fibo_series)
    print("Nilai Golden Ratio : ", goldenRatio)


if __name__ == "__main__":
    main()

