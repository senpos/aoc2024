from itertools import pairwise


def _is_report_safe(report):
    direction = None

    for a, b in pairwise(report):
        if b > a:
            if direction == -1:
                return False
            direction = 1
        elif a > b:
            if direction == 1:
                return False
            direction = -1
        else:
            return False

        distance = abs(a - b)
        if distance > 3:
            return False

    return True


safe_reports_count = 0

with open("input.txt") as f:
    for line in f:
        report = [int(level) for level in line.split()]
        safe_reports_count += _is_report_safe(report)

print(safe_reports_count)
