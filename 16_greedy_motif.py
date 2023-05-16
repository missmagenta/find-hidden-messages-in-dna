def greedymotifsearch(dna, k, t):
    bestmotifs = [string[:k] for string in dna]
    for j in range(len(dna[0]) - k + 1):
        motifs = [dna[0][j:j + k]]
        for i in range(1, t):
            motifs += [profile_most_probable_kmer(dna[i], k, profile(motifs))]
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs


def profile(motifs):
    transposed = [list(row) for row in zip(*motifs)]
    n = len(motifs)
    profile = {nucleotide: [i.count(nucleotide) / n for i in transposed] for nucleotide in 'ACGT'}
    return profile


def score(motifs):
    transposed = [list(row) for row in zip(*motifs)]
    counted = [[i.count(nucleotide) for nucleotide in 'ACGT'] for i in transposed]
    scored = sum([len(motifs) - max(i) for i in counted])
    return scored


def profile_most_probable_kmer(text, k, profile):
    probability = []
    for i in range(len(text) - k + 1):
        compute = 1
        for j in range(k):
            compute = compute * (profile[text[i + j]][j])
        probability.append(compute)
    idx = probability.index(max(probability))
    return text[idx:idx + k]


with open('dataset_240241_5 (2).txt', 'r') as f:
    line1 = f.readline().strip()
    k, t = map(int, line1.split())
    line2 = f.readline().strip()
    dna = line2.split()

print(" ".join(greedymotifsearch(dna, k, t)))
