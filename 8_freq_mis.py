def neighbors(pattern, d):  # return sequences with ham dist up to d
    nucleotides = ['A', 'C', 'T', 'G']  # creates a list of nucleotides
    if d == 0:  # if no mismatches
        return [pattern]  # returns a list containing input pattern as the only element
    if len(pattern) == 1:  # if length of pat = 1
        return nucleotides  # returns a list ['A', 'C', 'T', 'G']
    neighborhood = []  # empty list to store seqs
    suffix_neighbors = neighbors(pattern[1:], d)  # call func recursively with pattern that excludes its 1st char
    #  The reason why it excl 1st char - this allows func to generate all possible k-mers with up to d mismatches
    #  including k-mers that start with any of the four nucleotides (A, C, G, or T).
    for neigh in suffix_neighbors:  # iterates over all k-mers with up to d mismatches of the pattern
        if mismatches(pattern[1:], neigh) < d:  # for each neigh checks ham dist
            for n in nucleotides:  # iterates through all nucleotides
                neighborhood.append(n + neigh)  # appending each one to prefix (add one mismatch)
        else:
            neighborhood.append(pattern[0] + neigh)  # don't add new mismatch, take 1st char of pattern
    return neighborhood


def freq_words_mismatches(text, kmer_len, d):
    freq_map = {}
    for i in range(len(text) - kmer_len + 1):
        pattern = text[i:i+kmer_len]  # extracts kmer starting ar i and stores it in variable 'pattern'
        neighborhood = neighbors(pattern, d)  # finds neighbors
        for neigh in neighborhood:  # over all neighbors of current kmer in neighborhood list
            if neigh in freq_map:
                freq_map[neigh] += 1
            else:
                freq_map[neigh] = 1
    m = max(freq_map.values())
    most_freq = [k for k, count in freq_map.items() if count == m]
    return most_freq


def mismatches(p, s):  # the values pattern and seq[] are passed as args
    count = 0
    for i in range(len(p)):
        if p[i] != s[i]:
            count += 1
    return count


with open('dataset_9_9.txt') as f:
    lines = f.readlines()
    text = lines[0].strip()
    kmer_len = 6
    d = 2


print(freq_words_mismatches(text, kmer_len, d))









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
