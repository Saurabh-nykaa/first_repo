def ascending(**kwargs):
    ar1 = kwargs.get('ar1', [])
    zeroes = []
    ones = []
    twos = []

    for num in ar1:
        if num == 0:
            zeroes.append(num)
        elif num == 1:
            ones.append(num)
        else:
            twos.append(num)

    return zeroes + ones + twos  # Corrected the typo


arr = [0, 1, 2, 1, 2, 1, 2, 0, 1, 2, 1, 0, 1]
print(ascending(ar1=arr))
