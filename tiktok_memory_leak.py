import math


def find_root(a: int, b: int, c: int) -> int:
    dis = b * b - 4 * a * c
    val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        return (-b + val)/(2 * a)
    elif dis == 0:
        return (-b / (2 * a))


def brute_force(n1: int, n2: int, seconds: int) -> tuple:
    while True:
        # print(seconds, n1, n2)
        seconds += 1
        if n1 >= n2:
            if seconds > n1:
                return (seconds, n1, n2)
            n1 -= seconds
        else:
            if seconds > n2:
                return (seconds, n1, n2)
            n2 -= seconds
    # return (seconds+1, n1, n2)


def leak(n1: int, n2: int) -> tuple:
    diff = abs(n1 - n2)
    seconds = 0
    if diff == 0:
        seconds, n1, n2 = brute_force(n1, n2, 0)
        return (seconds, n1, n2)

    seconds = math.ceil(find_root(1, 1, - 2 * diff))

    sub_at_most = (seconds * (seconds+1))//2
    if n1 > n2:
        n1 -= sub_at_most
    elif n2 > n1:
        n2 -= sub_at_most
    print(seconds, n1, n2)
    seconds, n1, n2 = brute_force(n1, n2, seconds)
    return (seconds, n1, n2)


if __name__ == "__main__":
    # n = int(input("test cases: \n"))
    # for i in range(n):
    #     x, y = [int(a) for a in input("Enter any 2 numbers : \n ").split()]
    #     seconds, n1, n2 = leak(x, y)
    #     print(seconds+1, n1, n2)
    n1 = 2
    n2 = 2
    print(leak(n1, n2))
    # print(brute_force(n1, n2, 0))
