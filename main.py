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
    result=inverted_index[term1].intersection(inverted_index[term2])
    return  list(result)

def or_op(term1,term2):
    result=inverted_index[term1].union(inverted_index[term2])
    return list(result)

def and_not_op(term1,term2):
    result=inverted_index[term1].difference(inverted_index[term2])
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


result_set = set(inverted_index.get(tokens[0], set()))

# Iterate through tokens and operators together
for i, op in enumerate(operators, start=1):
    if i < len(tokens):  # Ensure there's a next term to process
        next_set = set(inverted_index.get(tokens[i], set()))
        if op.upper() == "AND":
            result_set = and_op(result_set, next_set)
        elif op.upper() == "OR":
            result_set = or_op(result_set, next_set)
        elif op.upper() == "AND NOT":
            result_set = and_not_op(result_set, next_set)
        # Placeholder for "OR NOT" logic
        # elif op.upper() == "OR NOT":
        #     result_set = or_not_op(result_set, next_set, all_docs)

# Convert the result set to a list and sort it for consistent output
final_list = sorted(list(result_set))
print(final_list)