def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'T', 'G']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    hamming_result = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for neigh in suffix_neighbors:
        if mismatches(pattern[1:], neigh) < int(d):
            for n in nucleotides:
                neighborhood.append(n + neigh)
                hamming_result.append(mismatches(pattern[0] + neigh, n + neigh))
        else:
            neighborhood.append(pattern[0] + neigh)
            hamming_result.append(mismatches(pattern[0] + neigh, pattern[0] + neigh))
    return neighborhood


def mismatches(str1, str2):
    if len(str1) != len(str2):
        return -1
    ham_dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            ham_dist += 1
    return ham_dist


with open('dataset_240229_4.txt') as f:
    lines = f.readlines()
    pattern = lines[0].strip()
    d = lines[1].strip()


print(*neighbors(pattern, d))
