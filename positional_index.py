import os
import pickle

dataset_path='preprocessed_files'
words=[]

for file in os.listdir(dataset_path):
    if file.endswith('.txt'):
        file_path=os.path.join(dataset_path,file)

        with open(file_path,"r") as f:
            data=f.read().split()

        words.extend(data)


final_list=set(words)

positional_index={}

num=0
for word in final_list:
    word_position={}
    position=set()
    pos=0
    for file in os.listdir(dataset_path):
        pos+=1
        if file.endswith(".txt"):
            file_path=os.path.join(dataset_path,file)
            with open(file_path,"r") as k:
                data=k.read().split()
            if word in data:
                position.add(pos)
    word_position[file]=position
    positional_index[word]=word_position
    num+=1
    print(num)


with open("positional_index.pickle","wb") as pos_file:
    pickle.dump(positional_index,pos_file)

print(positional_index)
print(num)
