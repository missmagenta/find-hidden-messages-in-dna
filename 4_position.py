def position(genome, pattern):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions


with open('Vibrio_cholerae.txt') as f:
    genome = f.readline().strip()
    pattern = 'CTTGATCAT'


print(*position(genome, pattern))
