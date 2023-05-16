def approx_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        pattern_x = text[i:i+len(pattern)]
        if hamming_distance(pattern, pattern_x) <= int(d):
            count += 1
    return count


def hamming_distance(p, s):
    c = 0
    for i in range(len(p)):
        if p[i] != s[i]:
            c += 1
    return c


with open('dataset_240221_6.txt') as f:
    lines = f.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
    d = lines[2].strip()


print(approx_pattern_count(text, pattern, d))
