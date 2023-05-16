def distance_between_pattern_and_strings(pattern, dna):
    distance = 0
    for seq in dna:  # for each seq
        hamming_distance = float('inf')  # large value for comparison with discovered distances
        for i in range(len(seq) - len(pattern) + 1):
            pattern_all = seq[i:i+len(pattern)]  # all possible kmers in a seq
            current_dist = 0
            for j in range(len(pattern)):
                if pattern[j] != pattern_all[j]:
                    current_dist += 1
            if current_dist < hamming_distance:  # discovering minim current dist
                hamming_distance = current_dist
        distance += hamming_distance
    return distance


with open("../dataset_5164_1.txt") as inp:
    input_items = inp.read().strip().splitlines()
    pattern = input_items[0].strip()
    dna = input_items[1].strip().split()


print(distance_between_pattern_and_strings(pattern, dna))


