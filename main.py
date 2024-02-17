import pickle
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('inverted_index.pickle', 'rb') as k:
    inverted_index = pickle.load(k)

stop_words = set(stopwords.words("english"))
all_docs = set()
for doc_set in inverted_index.values():
    all_docs.update(doc_set)

def preprocessing_query(input_string):
    lower_case = input_string.lower()
    remove_punctuation = lower_case.translate(str.maketrans("", "", string.punctuation))
    tokenize = word_tokenize(remove_punctuation)
    filtered_token = [word for word in tokenize if word not in stop_words]
    return filtered_token

def perform_operation(terms, operators):
    if not terms:
        return set()

    current_result = inverted_index.get(terms[0], set())

    for i, op in enumerate(operators):
        next_term_set = inverted_index.get(terms[i + 1], set())
        if op == 'AND':
            current_result &= next_term_set
        elif op == 'OR':
            current_result |= next_term_set
        elif op == 'AND_NOT':
            current_result -= next_term_set
        elif op == 'OR_NOT':
            current_result.union(all_docs.difference(next_term_set))

    return current_result



x = int(input("Number of queries: "))
for i in range(x):
    input_string = input("Enter your query: ")
    operators = input("Enter operators separated by space: ").split()

    tokens = preprocessing_query(input_string)
    if len(tokens) <= len(operators):
        print("Invalid input: Number of terms should be more than the number of operators.")
        continue

    result_set = perform_operation(tokens, operators)
    print("Documents matching the query:", result_set)
