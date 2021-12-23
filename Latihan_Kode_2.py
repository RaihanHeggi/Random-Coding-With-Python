import unittest


def simple_parantheses(arr):
    bracket = {"(": ")", "[": "]", "{": "}"}

    temp = []
    # not equivalent size
    if len(arr) % 2 != 0:
        return False
    for x in arr:
        if x in bracket.keys():
            temp.append(x)
        else:
            if len(temp) > 0:
                a = temp.pop()
                if x != bracket[a]:
                    return False
            else:
                return False
    return True


def main():
    print(simple_parantheses("()"))
    print(simple_parantheses("()[]"))
    print(simple_parantheses("(}){"))


if __name__ == "__main__":
    main()
