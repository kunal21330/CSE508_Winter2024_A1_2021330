import os

dataset_path = 'text_files'
preprocessed_file_path = 'preprocessed_files'

print("Content of first 5 text files:")
text_files_count = 0
for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path = os.path.join(dataset_path, file)
        with open(file_path, 'r') as k:
            data = k.read()
            print(data)
            print("-------------------------------------------------------------------------------------")
            text_files_count += 1
            if text_files_count >= 5:
                break


print("\nContent of first 5 preprocessed files:")
preprocessed_files_count = 0
for file in os.listdir(preprocessed_file_path):
    if preprocessed_files_count >= 5:
        break
    if file.endswith('.txt'):
        file_path = os.path.join(preprocessed_file_path, file)
        with open(file_path, 'r') as f:
            P_data = f.read()
            print(P_data)
            print("-------------------------------------------------------------------------------------")
            preprocessed_files_count += 1
