def combination(n, arr):
    temp = []
    output = []
    items = arr

    def dfs(price, items):
        if len(temp) == 4:
            output.append(temp[:])
            return
        if items and price > 0:
            for item in items[0]:
                temp.append(item)
                dfs(price - item, items[1:])
                temp.pop()
            return
    dfs(n, items)
    return output


arr = [[2, 3], [4], [2, 3], [1, 2]]

print(combination(10, arr))
