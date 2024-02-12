import os


dataset_path = 'preprocessed_files'
words=[]

for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path=os.path.join(dataset_path,file)

        with open(file_path,"r") as f:
            data=f.read().split()

        words.extend(data)


final_list=list(set(words))

inverted_index={}

for word in final_list:
    
    documents = []
    for file in os.listdir(dataset_path):
        if file.endswith('.txt'):
            file_path=os.path.join(dataset_path,file)
            with open(file_path,"r") as k:
                data=k.read().split()
            if word in data:
                documents.append(file)
    inverted_index[word] = documents

#have to wait till it reads and add all the words in dictionary.

for term, documents in inverted_index.items():
    print(term, "->", ", ".join(documents))