def palindromeCheck(palindromeString):
    end = len(palindromeString) - 1
    for i in range(len(palindromeString)):
        if palindromeString[i] == palindromeString[end]:
            end -= 1
        else:
            return False
    return True


def main():
    trueValue = [True, True, False, False, True]
    stringTest = ["kodok", "aba", "ba", "bak", "a"]
    functionValue = []
    for x in stringTest:
        functionValue.append(palindromeCheck(x))
    if trueValue == functionValue:
        print("Program Benar")
        print(str(functionValue))
    else:
        print("Program Salah")
        print(str(functionValue))


if __name__ == "__main__":
    main()

