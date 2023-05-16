def skew_position(sequence):
    skew_list = [0]
    for i in range(len(sequence)):
        if sequence[i] == 'C':
            skew_list.append(skew_list[i] - 1)
        elif sequence[i] == 'G':
            skew_list.append(skew_list[i] + 1)
        else:
            skew_list.append(skew_list[i])
    return skew_list


def find_min():
    minimum_list = []
    skew_list = skew_position(sequence)
    minimum = min(skew_list)
    for i in range(len(sequence)):
        if skew_list[i] == minimum:
            minimum_list.append(i)
    return minimum, minimum_list


with open('dataset_240220_10.txt') as f:
    sequence = f.readline().strip()


minimum, minimum_list = find_min()
print("Minimum value: ", minimum)
print("Minimum list: ", minimum_list)
