# Output yang diinginkan ['igPay atinlay siay oolcay', 'hisTay siay ymay tringsay']


def reverse(text):
    text_split = text.split(" ")
    resultList = []
    for x in text_split:
        temp = ""
        j = len(x)
        for i in range(1, j):
            temp += x[i]
        temp += x[0] + "ay"
        resultList.append(temp)
    return " ".join(resultList)


def main():
    checkValue = ["Pig latin is cool", "This is my string"]
    resultList = []
    for x in checkValue:
        resultList.append(reverse(x))
    print(resultList)


if __name__ == "__main__":
    main()
