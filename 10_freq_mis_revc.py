def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'T', 'G']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for neigh in suffix_neighbors:
        if mismatches(pattern[1:], neigh) < d:
            for n in nucleotides:
                neighborhood.append(n + neigh)
        else:
            neighborhood.append(pattern[0] + neigh)
    return neighborhood


def reverse(seq):
    rule = ''.maketrans('ACTG', 'TGAC')
    complement = seq[::-1].translate(rule)
    return complement


def freq_words_mismatches(text, kmer_len, d):
    freq_map = {}
    for i in range(len(text) - kmer_len + 1):
        pattern = text[i:i+kmer_len]  # extracts kmer starting ar i and stores it in variable 'pattern'
        neighborhood = neighbors(pattern, d)  # finds neighbors
        for neigh in neighborhood:
            if neigh in freq_map:
                freq_map[neigh] += 1
            else:
                freq_map[neigh] = 1

        rev_pattern = reverse(pattern)
        rev_neigh = neighbors(rev_pattern, d)
        for neigh in rev_neigh:
            if neigh in freq_map:
                freq_map[neigh] += 1
            else:
                freq_map[neigh] = 1
    m = max(freq_map.values())
    most_freq = [k for k, count in freq_map.items() if count == m]
    return most_freq


def mismatches(p, s):
    count = 0
    for i in range(len(p)):
        if p[i] != s[i]:
            count += 1
    return count


with open('dataset_240221_10.txt') as f:
    lines = f.readlines()
    text = lines[0].strip()
    kmer_len = 5
    d = 3


print(*freq_words_mismatches(text, kmer_len, d))











# Neighbors func is a recursive that generates all possible k-mers with up to d mismatches of a given pattern.
# The reason why it excl the 1st char - this allows the func to generate all possible k-mers with up to d mismatches,
# including k-mers that start with any of the four nucleotides (A, C, G, or T).
# For example, let's say the original pattern is "ACGT".
# If we were to generate all possible k-mers with up to d mismatches of "ACGT" directly,
# we would need to consider all 4^4 = 256 possible combinations,
# which would be very computationally expensive for larger values of k and d.
# However, by recursively calling Neighbors with the pattern "CGT" (which is pattern[1:]),
# we can generate all possible k-mers with up to d mismatches of "CGT",
# and then append each of 4 nucleotides to the beginning of each generated k-mer to get all possible k-mers of "ACGT".
# This approach greatly reduces the number of combinations that need to be considered.
# So in essence, by recursively calling Neighbors with pattern[1:],
# the function is able to generate all possible k-mers with up to d mismatches in a more efficient way.
