import pandas as pd
data = pd.read_csv('dataset_2_6.txt', names=["data"])  # set name of single col,func looks at 1 row to determ col names


def pattern_text(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count


print("Number of times we find out a given pattern: ", pattern_text((data["data"][0]), data["data"][1]))
# data["data"] accesses the column of data, [0] accesses first element in that column (first line of letters in file)
# the PatternText function is being called with the first line of data (data["data"][0]) as the Text argument,
# and the second line of data (data["data"][1]) as the Pattern argument.
# The function then counts the number of times that the Pattern appears in the Text using a sliding window approach.


def pattern_count():
    c = 0
    with open('dataset_2_6.txt') as f:
        # context manager, creating a file object f, with ensures that file is properly closed after you're done with it
        lines = f.readlines()
        text = lines[0].strip()
        pattern = lines[1].strip()
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)] == pattern:
                c += 1
    return c


print("Number of times we find out a given pattern: ", pattern_count())
