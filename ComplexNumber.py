import cmath as c

def main():
    inputValue = complex(input().strip())
    print(c.polar(inputValue)[0])
    print(c.polar(inputValue)[1])

if __name__ == "__main__":
    main()
    