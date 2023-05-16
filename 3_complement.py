def complement():
    with open('dataset_240215_2.txt') as f:
        seq = f.readline().strip()
        rule = ''.maketrans('ACTG', 'TGAC')
        compl = seq[::-1].translate(rule)
        return compl


print(complement())
