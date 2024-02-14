import pickle
import string 
import nltk
from nltk.corpus import stopwords

with open('inverted_index.pickle','rb') as k:
    inverted_index=pickle.load(k)

stop_words=set(stopwords.words("english"))
def preprocessing_query(input_string):
    lower_case = input_string.lower()
    remove_punctuation = lower_case.translate(str.maketrans("", "", string.punctuation))
    tokenize = nltk.word_tokenize(remove_punctuation)
    filtered_token = [word for word in tokenize if not (word in stop_words)]
    return filtered_token

def and_op(term1,term2):
    result=inverted_index.get(term1).intersection(inverted_index.get(term2))
    return  list(result)

def or_op(term1,term2):
    result=inverted_index.get(term1).union(inverted_index.get(term2))
    return list(result)

def and_not_op(term1,term2):
    result=inverted_index.get(term1).difference(inverted_index.get(term2))
    return list(result)

def op_or_not(term1, term2, all_docs):
    result=term1.union(all_docs.difference(term2))
    return result


x=int(input("no of query:"))
for i in range(0,x):
    input_string=input()
    operators=input().split()

tokens=preprocessing_query(input_string)

tokens=list(tokens)
temp_list=[]

for i in range(len(tokens)-1):
    if(operators[i]=="AND"):
        temp_list=and_op(tokens[i],tokens[i+1])
    elif(operators[i]=="OR"):
        temp_list=or_op(tokens[i],tokens[i+1])
    elif(operators[i]=="AND NOT"):
        temp_list=and_not_op(tokens[i], tokens[i + 1])
    # elif(operators[i]=="OR NOT"):
    #     final_list.append(op_or_not(tokens[i],tokens[i+1],))

print(temp_list)