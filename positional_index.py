import os
import pickle

dataset_path = 'preprocessed_files'
words = []

# Collect all words from all files
for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path = os.path.join(dataset_path, file)
        with open(file_path, "r") as f:
            data = f.read().split()
        words.extend(data)

final_list = set(words)
positional_index = {}

num=1
# Create positional index
for word in final_list:
    word_position = {}  # This will map file to positions of the word
    for file in os.listdir(dataset_path):
        if file.endswith(".txt"):
            file_path = os.path.join(dataset_path, file)
            with open(file_path, "r") as k:
                data = k.read().split()
            if word in data:
                # Find all positions of word in data
                positions = [i for i, x in enumerate(data) if x == word]
                if positions:
                    word_position[file] = positions  # Store positions for each file
    if word_position:
        positional_index[word] = word_position

    num+=1
    print(num)

# Save positional index to pickle file
with open("positional_index.pickle", "wb") as pos_file:
    pickle.dump(positional_index, pos_file)

print(positional_index)