from math import frexp


NUMBERS = [
    ('M', 1000),
    ('D', 500),
    ('C', 100),
    ('L', 50),
    ('X', 10),
    ('V', 5),
    ('I', 1),
]

for index, number in enumerate(NUMBERS[:]):
    if number[1] == 1:
        break

    index = index * 2 + 1

    decimal = 1
    for i in range(4):
        if NUMBERS[index][1] == 10 ** i:
            decimal = 0
    decimal += index

    NUMBERS.insert(
        index,
        (NUMBERS[decimal][0] + number[0], number[1] - NUMBERS[decimal][1])
    )

def to_roman(number):
    roman = ''
    for letter, decimal in NUMBERS:
        while number >= decimal:
            roman += letter
            number -= decimal
    return roman
