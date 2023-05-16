def Entropy(Motifs):
    Profile = {}
    # check that all motifs are the same length
    ListLength = len(Motifs)
    L1 = len(Motifs[1])  # length of the first motif
    print('There are {} motifs of length {}'.format(ListLength, L1))
    for i in range(len(Motifs)):
        if len(Motifs[i]) != L1:
            ShortMotif = Motifs[i]
            ShortMotifLen = len(ShortMotif)
            print(' Motif {} is {} nucleotides instead of {}!'.format(ShortMotif, ShortMotifLen, L1))
            break

    # fill all positions with frequency of 0
    for nucleotide in 'ACGT':
        values = [0] * L1
        Profile[nucleotide] = values

    # iterate through each position in the motif matrix, counting nucleotide frequencies
    TotalEntropy = 0
    for key, values in Profile.items():
        for Motif in Motifs:
            for i in range(len(Motif)):
                if Motif[i] == key:
                    Profile[key][i] += 1

        # convert nucleotide frequencies to probabilities
        for i in range(len(values)):
            Profile[key][i] = Profile[key][i] / float(ListLength)

        # calculate total entropy (Sum of (Prob_value * log2 Prob_n))
        import math
        for value in values:
            if value > 0:
                TotalEntropy += abs(value * math.log(value, 2))
            else:
                continue

    return (TotalEntropy)


Motifs1 = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]

Motifs2 =[
    "TCATATTTTT",
    "CCCTATCCAC",
    "GGGGGGGGGG",
    "GGGGGGGGGG",
    "GTGGGGGGGG",
    "GGGGGGGGGT",
    "GAAAAAAAAA",
    "TCTCCCTTAT",
    "TTTTTTTTCA",
    "TTTTTTCCTA",
    "TATTCCACAC",
    "TCCTCCTTCC"
]

print(Entropy(Motifs2))
print(Entropy(Motifs1))

import numpy as np
import math

CHARS = "ACGT"


motifs = Motifs1
# Output: profiles
def computer_profile(motifs) -> dict:
    counts = {}
    profiles = {}
    columns = len(motifs[0])
    rows = len(motifs)

    for c in CHARS:
        counts[c] = np.zeros(columns)
        profiles[c] = list(np.zeros(columns))

    for i in range(columns):
        for j in range(rows):
            counts[motifs[j][i]][i] += 1

    for i in range(columns):
        s = counts[CHARS[0]][i] + counts[CHARS[1]][i] + counts[CHARS[2]][i] + counts[CHARS[3]][i]
        for x in CHARS:
            profiles[x][i] = counts[x][i] / s

    return profiles


# Input: motifs
# Output: entropy
def compute_entropy(motifs) -> float:
    p = computer_profile(motifs)
    e = {}
    columns = len(motifs[0])
    for char in CHARS:
        for i in range(columns):
            x = p[char][i]
            if x:
                if x in e:
                    e[x] += 1
                else:
                    e[x] = 1

    ent = 0
    for x in e:
        ent += e[x] * x * math.log2(x)

    return (-1)*ent
print("Entropy: ", compute_entropy(motifs))


import math


lst = Motifs1
def calc_entropy(lst):
    return round(-sum([x*math.log2(x) for x in lst if x > 0]), 4)

def entropy(motifs):
    entropy = []
    transpose = [''.join(s) for s in zip(*motifs)] # transposes strings into rows
    for row in transpose:
        lst = []
        for base in 'acgt':
            lst.append(row.lower().count(base)/len(row))
        entropy.append(calc_entropy(lst))
    return sum(entropy)
print("Entropy is :", entropy(lst))

import numpy as np


def entropy(prop):
    return np.sum([-x * np.log2(x) for x in prop if x > 0])


def motif_entropy(motifs, dna=True):
    n = len(motifs[0])
    result = 0
    for i in range(n):
        nucleotides = "ATGC"
        freq = {k: 0 for k in nucleotides}
        for motif in motifs:
            freq[motif[i]] += 1
        tot = sum(list(freq.values()))
        result += entropy([v / tot for v in freq.values()])
    return result
print(motif_entropy(motifs))


def Entropy(Motifs):
    import math
    entropy_profile_matrix = 0
    for pos in range(len(Motifs[0])):
        entropy_col_pos = 0
        for symbol in 'ACGT':
            try:
                entropy_col_pos += (profile(Motifs)[symbol][pos]) * math.log2((Profile(Motifs)[symbol][pos]))
            except ValueError:
                entropy_col_pos += 0
        entropy_profile_matrix += entropy_col_pos
    entropy_profile_matrix *= -1
    return entropy_profile_matrix
print(Entropy(motifs))
