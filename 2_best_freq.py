def frequency_table(text, k):
    freq_map = {}
    n = len(text)
    for i in range(n - int(k) + 1):
        pattern = text[i:i+int(k)]
        if pattern in freq_map:
            freq_map[pattern] += 1
        else:
            freq_map[pattern] = 1
    return freq_map


def better_freq_words(text, k):
    freq_patterns = []
    freq_map = frequency_table(text, k)
    m = max(freq_map.values())
    for pattern in freq_map:
        if freq_map[pattern] == m:
            freq_patterns.append(pattern)
    return freq_patterns


with open('dataset_240214_13.txt') as f:
    lines = f.readlines()
    text = lines[0].strip()
    k = lines[1].strip()


print(*better_freq_words(text, k))
