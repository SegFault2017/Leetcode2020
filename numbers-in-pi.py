def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float('inf') else minSpaces


def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float('inf')
    for i in range(idx, len(pi)):
        prefix = pi[idx:i + 1]
        if prefix in numbersTable:
            minSpacesInSiffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSiffix + 1)
    cache[idx] = minSpaces
    return cache[idx]


if __name__ == "__main__":
    pi = "3141592653589793238462643383279"
    numbers = ["314159265358979323846", "26433", "8",
               "3279", "314159265", "35897932384626433832", "79"]
    print(numbersInPi(pi, numbers))
