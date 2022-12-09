import random

number = str(random.randint(0, 1))
for _ in range(3):
    number += str(random.randint(0, 1))

print(number)

# converting the number to base 10
def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


# Enter values belwo
# print(number_to_base(int(number), 2))
