import os
import string
import nltk
from nltk.corpus import stopwords


nltk.download('punkt')

dataset_path='text_files'
stop_words = set(stopwords.words('english'))

translator = str.maketrans('','',string.punctuation)

for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path=os.path.join(dataset_path,file)


        raw_data=nltk.data.load(file_path,format='text')


        lowercase=raw_data.lower()


        tokenized=nltk.word_tokenize(lowercase)


        filtered_tokens = [token for token in tokenized if token not in stop_words]


        removepanctuation=[word.translate(translator) for word in filtered_tokens]


        Preprocessed_file_path = os.path.join('preprocessed_files','preprocessed_'+ file)
        with open(Preprocessed_file_path,'w') as f:
            f.write(' '.join(removepanctuation))