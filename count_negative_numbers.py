given_numbers = [7, 5, 4, 2, 1, -1, -3, -4, -7, -11]

# using for loop
total_for = 0
for number in given_numbers:
    if number < 0:
        total_for += number

print(total_for)

# using while loop
total_while = 0
i = 0
while i < len(given_numbers):
    if given_numbers[i] < 0:
        total_while += given_numbers[i]
    i += 1

print(total_while)