def compute_probability(kmer, profile_mat):
    prob = 1
    for i in range(0, len(kmer)):
        if kmer[i] == 'A':
            prob = prob * profile_mat[0][i]
        if kmer[i] == 'C':
            prob = prob * profile_mat[1][i]
        if kmer[i] == 'G':
            prob = prob * profile_mat[2][i]
        if kmer[i] == 'T':
            prob = prob * profile_mat[3][i]
    return prob


def profile_most_probable_kmer(text, k, profile):
    n = len(text)
    pr = {}
    most_prob_kmer = []
    for i in range(n - k + 1):
        k_mer = text[i:i + k]
        probability = compute_probability(k_mer, profile)
        pr[k_mer] = probability
    m = max(pr.values())
    for key, value in pr.items():
        if pr[key] == m:
            most_prob_kmer.append(key)
    return most_prob_kmer[0]


filename = 'dataset_240241_3.txt'
with open(filename, "r") as dataset:
    data = []
    for line in dataset:
        data.append(line.strip())
    Text = data[0]
    k = int(data[1])
    raw_profile = data[2:]
    bases = ['A', 'C', 'G', 'T']
    profile_mat = [list(map(float, raw_profile[i].split())) for i in range(len(raw_profile))]
    prof_dict = dict(zip(bases, profile_mat))
    print(profile_mat)

print(profile_most_probable_kmer(Text, k, profile_mat))
