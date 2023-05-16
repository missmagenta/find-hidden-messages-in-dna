with open('Ecoli.txt', 'r') as f:
    lines = f.readlines()
    genome = lines[0].strip()
f.close()
k = 9  # pattern length
L = 500  # window length
t = 3  # at least t times


def frequency_map(genome, k):
    freq_map = {}  # dictionary
    for i in range(len(genome) - k + 1):  # moving a window
        pattern = genome[i:i + k]  # set patterns
        if pattern in freq_map:
            freq_map[pattern] += 1
        else:
            freq_map[pattern] = 1
    return freq_map


def find_clumps(genome, k, L, t):
    clumps = []
    count = 0
    for i in range(0, len(genome) - L):
        window = genome[i:i+L]  # check how many times this pattern is in area of len L
        freq = frequency_map(window, k)  # calling a prev func
        for pattern in freq:  # for a value in dict
            if freq[pattern] >= t:
                if pattern not in clumps:  # adding the same seq once to one clump
                    clumps.append(pattern)
                    count += 1
    return count, clumps


count, clumps = find_clumps(genome, k, L, t)
print(*clumps)
print(count)
