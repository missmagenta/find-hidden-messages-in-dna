def hamming(p, s):
    return sum([p[i] != s[i] for i in range(len(s))])


def distance_between_pattern_and_strings(DNA, pattern):
    final_dist = 0
    for seq in DNA:
        d_list = []
        for j in range(len(seq) - len(pattern) + 1):
            d = hamming(pattern, seq[j: j + len(pattern)])
            d_list.append(d)
        final_dist += min(d_list)
    return final_dist


def median_string(DNA, K):
    final_pattern = ''
    for e in range(len(DNA[0]) - K + 1):
        current_pattern = DNA[0][e: e + K]
        current_dist = distance_between_pattern_and_strings(DNA, current_pattern)
        if e == 0:
            min_dist = current_dist
            final_pattern = current_pattern
        else:
            if current_dist < min_dist:
                min_dist = current_dist
                final_pattern = current_pattern
    return final_pattern


with open("dataset_240240_9.txt") as inp:
    input_items = inp.read().strip().splitlines()
    k = int(input_items[0].strip())
    dna = [i.strip() for i in input_items[1:]]
print(median_string(dna, k))




