def mismatches(p, s):  # the values pattern and seq[] are passed as args
    count = 0
    for i in range(len(p)):
        if p[i] != s[i]:
            count += 1
    return count


def starting_points(pattern, seq, d):
    points_list = []
    for i in range(len(seq) - len(pattern) + 1):
        if mismatches(pattern, seq[i:i + len(pattern)]) <= int(d):
            points_list.append(i)
            length = len(points_list)
    return length, points_list


with open('dataset_240221_4.txt') as f:
    lines = f.readlines()
    pattern = lines[0].strip()
    seq = lines[1].strip()
    d = lines[2].strip()


length, points_list = starting_points(pattern, seq, d)
print(f"{length}\n{points_list}")
