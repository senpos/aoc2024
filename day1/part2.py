from collections import Counter, defaultdict

left, right = [], []


with open("input.txt") as f:
    for line in f:
        a, b = line.split(maxsplit=1)
        left.append(int(a))
        right.append(int(b))

right_counter = Counter(right)

scrores_per_number = defaultdict(int)
for a in left:
    scrores_per_number[a] += a * right_counter.get(a, 0)

similarity_score = sum(scrores_per_number.values())
print(similarity_score)
