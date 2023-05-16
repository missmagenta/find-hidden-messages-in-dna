def greedy_motif_search(dna, k, t):
    best_motifs = []
    for str in range(t):
        best_motifs.append(dna[str][0:k])  # first kmers in each dna string - serves as initial set of motifs
        """
        By starting with the first k-mers of each string, we have some initial candidate motifs to begin with,
        and we can iteratively update these motifs to try and find a better set of motifs that gives the best score.
        it is a common practice to choose the first k-mer of each DNA string as the initial set of motifs because it is likely to contain some signal that could potentially represent a motif in the DNA sequences.
        For example, if the DNA sequences represent regulatory regions, the first k-mer may correspond to a transcription factor binding site or other regulatory motif.
        """
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]
        # For each start pos, the motifs list is initialized to contain only the first k-mer of the first DNA sequence.
        for j in range(1, t):
            profile = profile_matrix(motifs)
            motifs.append(profile_most_probable_pattern(dna[j], k, profile))
            """
            Iteratively add the most probable k-mer from each subsequent DNA sequence based on the current motif profile.
            """
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


def profile_matrix(motifs):
    k = len(motifs[0])  # all motifs have the same length
    profile = {'A': [1] * k, 'C': [1] * k, 'G': [1] * k, 'T': [1] * k}
    """ dictionary with 4 keys, each key is assoc with list of k zeros,
    which represents the count of nucleotides at each position in the motif """
    for i in range(k):  # loops over each position
        for j in range(len(motifs)):  # loop over each motif in Motifs []
            profile[motifs[j][i]][i] = profile[motifs[j][i]][i] + 1 / len(motifs)
            """
            Motifs[j][i] accesses the nucleotide at position i of the j-th motif in Motifs
            which is used as a key to the corresponding list of counts in Profile
            Profile[Motifs[j][i]][i] accesses the count of the nucleotide at position i for the j-th motif
            and += 1/len(Motifs) - 1/number of motifs in Motifs
            results in frequency of the nucleotide at pos i
            the second [i] at the end of the line refers to the index of the list within the Profile dictionary that corresponds to the nucleotide at the ith position in the motif.
            For example, if Motifs[j][i] is 'A', then Profile['A'] retrieves the list of nucleotide counts for the nucleotide 'A'. 
            The second [i] then updates the count for the nucleotide 'A' at the ith position in the motif.
            
            """
    return profile


def profile_most_probable_pattern(text, k, profile):
    max_prob = -1  # ensure that the 1st probability is greater than that
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        prob = 1
        for j in range(k):
            prob = prob * profile[pattern[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_pattern = pattern
    return most_probable_pattern


def score(motifs):
    t = len(motifs)
    k = len(motifs[0])
    consensus = ""
    for i in range(k):
        count = {"A": 0, "C": 0, "G": 0, "T": 0}
        for j in range(t):
            count[motifs[j][i]] += 1
        max_count = max(count.values())
        for base, count in count.items():
            if count == max_count:
                consensus += base
                break
    score = 0
    for i in range(t):
        for j in range(k):
            if motifs[i][j] != consensus[j]:
                score += 1
    return score


with open('dataset_240242_9.txt', 'r') as f:
    line1 = f.readline().strip()
    k, t = map(int, line1.split())
    line2 = f.readline().strip()
    dna = line2.split()


best_motifs = greedy_motif_search(dna, k, t)
print(" ".join(best_motifs))


#     split() - to split the string line into a list of substrings based on a delimiter (whitespace by default).
#     line contains two integers separated by a whitespace, so calling line.split() returns a list of two strings:
#     the first string represents the value of k and the second string represents the value of t.
#     The map() function is then used to apply the int() function to each element of the list returned by split(),
#     which converts the strings to integers.
