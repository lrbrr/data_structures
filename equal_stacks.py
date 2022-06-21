def equalStacks(h1, h2, h3):
    if len(h1) == 0 or len(h2) == 0 or len(h3) == 0: return 0

    h1_sum = [sum((h1[::-1])[:i+1]) for i in range(len(h1))]
    h2_sum = [sum((h2[::-1])[:i+1]) for i in range(len(h2))]
    h3_sum = [sum((h3[::-1])[:i+1]) for i in range(len(h3))]

    smallest_array = h1_sum if len(h1_sum) < len(h2_sum) else h2_sum
    smallest_array = smallest_array if len(smallest_array) < len(h3_sum) else h3_sum

    for i in range(len(smallest_array)-1, -1, -1):
        if smallest_array[i] in h1_sum and smallest_array[i] in h2_sum and smallest_array[i] in h3_sum:
            return smallest_array[i]
    return 0

print(equalStacks([1, 2, 1, 1], [1, 1, 2], [1, 1])) # 2
print(equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1])) # 5