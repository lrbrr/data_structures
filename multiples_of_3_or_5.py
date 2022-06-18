# Calculate the sum of multiples of 3 or 5 between 1 and 100

total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)