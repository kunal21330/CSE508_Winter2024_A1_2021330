import pickle
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_query(input_string):
    """
    Preprocess the input string: tokenize, convert to lowercase,
    remove punctuation, and filter out stopwords.
    """
    # Tokenize and preprocess the input string
    tokens = word_tokenize(input_string)
    lower_case = [word.lower() for word in tokens]
    remove_punctuation = [word.translate(str.maketrans("", "", string.punctuation)) for word in lower_case]
    filtered_tokens = [word for word in remove_punctuation if word not in stop_words and word != '']
    return filtered_tokens

# Load the positional index from a file
with open('positional_index.pickle', 'rb') as file:
    positional_index = pickle.load(file)

stop_words = set(stopwords.words("english"))

number_of_queries = int(input("Number of queries: "))
for _ in range(number_of_queries):
    input_string = input("Enter your query: ")
    query_tokens = preprocess_query(input_string)

    # Execute phrase query directly here
    documents_positions = {}
    if query_tokens:
        term = query_tokens[0]
        documents_positions = positional_index.get(term, {})
        for term in query_tokens[1:]:
            if term not in positional_index:
                documents_positions = {}
                break  # Term not in index, phrase cannot be found
            new_documents_positions = {}
            for doc, positions in positional_index[term].items():
                if doc in documents_positions:
                    for prev_position in documents_positions[doc]:
                        if isinstance(prev_position, int):
                            prev_position = [prev_position]  # Ensure prev_position is a list
                        new_positions = [pos for pos in positions if pos - 1 in prev_position]
                        if new_positions:
                            new_documents_positions.setdefault(doc, []).extend(new_positions)
            documents_positions = new_documents_positions

    results = list(documents_positions.keys())
    print(f"Query: {input_string}")
    print(f"Number of documents retrieved: {len(results)}")
    if results:
        print("Documents:")
        for doc in results:
            positions = positional_index[query_tokens[-1]].get(doc, [])
            print(f"- Document ID: {doc}, Positions: {positions}")
    else:
        print("No documents found.")
    print()
