left, right = [], []


with open("input.txt") as f:
    for line in f:
        a, b = line.split(maxsplit=1)
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

total_distance = 0
for a, b in zip(left, right):
    total_distance += abs(a - b)

print(total_distance)
