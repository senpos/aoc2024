import re

with open("input.txt") as f:
    memory = f.read()

mul_pairs = re.findall(r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)", memory)
result = sum(int(a) * int(b) for a, b in mul_pairs)
print(result)
