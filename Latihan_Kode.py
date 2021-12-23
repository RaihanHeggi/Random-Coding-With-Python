import unittest


def binary_search(arr, low, high, x):
    # we can achieve this searching with time complexity only O(logn)
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1


def linear_search(arr, x):
    # because in line or loop until N so the time complexity is O(n)
    for j in arr:
        if j == x:
            return arr.index(j)
    return -1


def selection_sort(arr):
    temp = 0
    for i in range(0, len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr


def bubble_sort(arr):
    temp = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def main():
    arr = [3, 4, 5, 6, 7, 8, 9]
    data = [-2, 45, 0, 11, -9]
    x = 4

    result_binary = binary_search(arr, 0, len(arr) - 1, x)
    result_linear = linear_search(arr, x)

    print(result_binary)
    print(result_linear)

    print(selection_sort(data))
    print(bubble_sort(data))


class TestSum(unittest.TestCase):
    def test_search(self):
        arr = [3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 0, len(arr), 4), 1)
        self.assertEqual(linear_search(arr, 4), 1)


if __name__ == "__main__":
    unittest.main()
