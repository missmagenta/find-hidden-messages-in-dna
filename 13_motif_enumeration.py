def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for neigh in suffix_neighbors:
        if hamming_distance(pattern[1:], neigh) < d:
            for n in nucleotides:
                neighborhood.append(n + neigh)
        else:
            neighborhood.append(pattern[0] + neigh)
    return neighborhood


def motif_enumeration(dna, k, d):
    patterns = []
    for i in range(len(dna[0]) - k + 1):  # dna[0] - 1st element in the list
        call_neighbors = neighbors(dna[0][i:i + k], d)  # loop over each pos,generate all possible d-neighborhoods len k
        for neigh in call_neighbors:
            count = 0
            for seq in dna:
                for j in range(len(seq) - k + 1):
                    if hamming_distance(neigh, seq[j:j+k]) <= d:
                        count += 1
                        break
            if count == len(dna):  # if kmer appears in each sequence in the list
                patterns.append(neigh)
    return patterns


with open('dataset_240238_8.txt') as f:
    line1 = f.readline().strip()
    k, d = map(int, line1.split())
    line2 = f.readline().strip()
    dna = line2.split()


print(motif_enumeration(dna, k, d))

patterns = motif_enumeration(dna, k, d)
patterns = list(set(patterns))
print("Using list(set): ", patterns)

without_duplicates = []
[without_duplicates.append(x) for x in patterns if x not in without_duplicates]
# When you list comprehension like [without_duplicates.append(x) for x in patterns if x not in without_duplicates],
# you are adding multiple elements to the list in a single line of code.
# The result of the list comprehension is a list of values, one for each iteration of the loop.
# By enclosing the list comprehension in [], you are collecting these values into a list.
# If you omit the square brackets, you would only get a single value, corresponding to the last iteration of the loop.
print("List comprehension: ", without_duplicates)


# [without_duplicates.append(x) for x in patterns if x not in without_duplicates] is less efficient than the 1st option:
# It creates a list comprehension, which creates a new list object in memory,
# and then appends to without_duplicates in each iteration.
# This can lead to a lot of unnecessary memory allocation and deallocation.
# It uses the in operator to check if an element is already in without_duplicates for every element in patterns.
# This is an O(n^2) operation, which is less efficient than the O(n) operation performed by the first option.
# It's less pythonic because it uses list comprehension for its side effect of appending elements to without_duplicates,
# which goes against the principle of using list comprehensions for creating new lists.
# Overall, the first option is the most efficient and pythonic way to remove duplicates from a list.
# It is more concise, easier to read, and performs better than the third option.
