import re

with open("input.txt") as f:
    memory = f.read()


_INSTR = r"""
    (?P<name>mul|don't|do)
    \(
        (?P<args>(\d+,?)+)?
    \)
"""


total = 0
is_mul_enabled = True

for instr in re.finditer(_INSTR, memory, re.X):
    name = instr["name"]

    args = instr["args"]
    if args:
        args = args.split(",")

    if name == "mul":
        if is_mul_enabled:
            a, b = map(int, args)
            total += a * b
    elif name == "do":
        is_mul_enabled = True
    elif name == "don't":
        is_mul_enabled = False
    else:
        raise ValueError(f"unknown instruction {name!r}")

print(total)
