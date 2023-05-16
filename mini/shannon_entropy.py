from math import log2

def calculate_entropy(distribution):
    entropy_sum = 0
    for probability_event in distribution:
        if probability_event != 0:
            entropy_sum += -probability_event*log2(probability_event)
    return entropy_sum

distribution_1 = [4/8, 3/8, 1/8]
entropy_1 = calculate_entropy(distribution_1)
print(entropy_1)                                 # 1.4056390622295665

distribution_2a = [1/2, 1/2]
distribution_2b = [3/4, 1/4]
entropy_2a = calculate_entropy(distribution_2a)
entropy_2b = calculate_entropy(distribution_2b)
print(entropy_2a)                                # 1.0
print(entropy_2b)                                # 0.8112781244591328
print(entropy_2a + 0.5* entropy_2b)              # 1.4056390622295665