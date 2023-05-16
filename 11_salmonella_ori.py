# with open('Salmon.fasta', 'r') as f:
#     f.readline()  # read the 1st line (header) and skips it
#     seq_lines = [line.strip() for line in f.readlines()]  # strip() deletes whitespaces from beginning & end of line
# seq = ''.join(seq_lines)  # join concretes elements into single line, '' - separator bw elems = without any separator
# with open('Salmon_out.fasta', 'w') as f:
#     f.write(seq)
# f.close()

with open('Salmon_out.fasta') as f:
    lines = f.readlines()
    text = lines[0].strip()
    kmer_len = 9
    d = 1


def skew_position(text):
    skew_list = [0]
    for i in range(len(text)):
        if text[i] == 'C':
            skew_list.append(skew_list[i] - 1)
        elif text[i] == 'G':
            skew_list.append(skew_list[i] + 1)
        else:
            skew_list.append(skew_list[i])
    return skew_list


def find_min():
    minimum_list = []
    skew_list = skew_position(text)
    minimum = min(skew_list)
    for i in range(len(text)):
        if skew_list[i] == minimum:
            minimum_list.append(i)
    return minimum, minimum_list


minimum, minimum_list = find_min()
print("Minimum value: ", minimum)
print("Minimum list: ", minimum_list)


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
    for i in range((len(text) - kmer_len + 1)):
        pattern = text[i:i+kmer_len]
        neighborhood = neighbors(pattern, d)
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


center = minimum_list[0]
rad1 = 500
rad2 = 1000
rad3 = 200
rad4 = 2000
rad5 = 100

subseq1 = text[center - rad1: center + rad1]
subseq2 = text[center - rad2: center + rad2]
subseq3 = text[center - rad3: center + rad3]
subseq4 = text[center - rad4: center + rad4]
subseq5 = text[center - rad5: center + rad5]


def mismatches(p, s):
    count = 0
    for i in range(len(p)):
        if p[i] != s[i]:
            count += 1
    return count


print("Radius is 500 bp: ", freq_words_mismatches(subseq1, kmer_len, d))
print("Radius is 1000 bp: ", freq_words_mismatches(subseq2, kmer_len, d))
print("Radius is 200 bp: ", freq_words_mismatches(subseq3, kmer_len, d))
print("Radius is 2000 bp: ", freq_words_mismatches(subseq4, kmer_len, d))
print("Radius is 100 bp: ", freq_words_mismatches(subseq5, kmer_len, d))
