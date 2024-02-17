import os
import pickle


dataset_path = 'preprocessed_files'
words=[]

for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path=os.path.join(dataset_path,file)

        with open(file_path,"r") as f:
            data=f.read().split()

        words.extend(data)


final_list=set(words)

inverted_index={}

num=0
for word in final_list:
    
    documents = set()
    for file in os.listdir(dataset_path):
        if file.endswith('.txt'):
            file_path=os.path.join(dataset_path,file)
            with open(file_path,"r") as k:
                data=k.read().split()
            if word in data:
                documents.add(file)
    inverted_index[word] = documents
    num+=1
    print(num)

#have to wait till it reads and add all the words in dictionary.
    
with open("inverted_index.pickle","wb") as inv_file:
    pickle.dump(inverted_index,inv_file)

