import os
import nltk

dataset_path='text_files'

for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path=os.path.join(dataset_path,file)

        raw_data=nltk.data.load(file_path,format='text')

        lowercase=raw_data.lower()

        Preprocessed_file_path = os.path.join(dataset_path,'preprocessed_'+ file)
        with open(Preprocessed_file_path,'w') as f:
            f.write(raw_data)