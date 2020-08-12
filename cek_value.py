
def main() :
    string = "abcdcdcdcbcdc" 
    substring = "cdc"
    iteration = 0
    new_loops = 0
    a = ""
    for i in range(len(string)): 
        new_loops = i
        for j in range(len(substring)):
            if(new_loops > len(string)):
                break
            a = a + string[new_loops-1]
            new_loops += 1
        print(a)
        if(a == substring): 
            iteration += 1
        new_loops = 0
        a = ""
    print(iteration)

if __name__ == "__main__":
    main()