import pickle

with open('positional_index.pickle', 'rb') as file:
    positional_index = pickle.load(file)

def execute_phrase_query_without_preprocessing(query, positional_index):
    terms = query.split()  # Assuming query is a space-separated string of preprocessed terms
    documents_positions = {}  # Document: [positions]

    # Initialize documents_positions with positions of the first term
    if terms[0] in positional_index:
        for doc, positions in positional_index[terms[0]].items():
            documents_positions[doc] = [positions]

    # For each subsequent term, refine the search
    for term in terms[1:]:
        if term not in positional_index:
            return []  # If any term is not in the index, the phrase can't be found
        new_documents_positions = {}
        for doc, positions in positional_index[term].items():
            if doc in documents_positions:
                for prev_positions in documents_positions[doc]:
                    new_positions = [pos for pos in positions if pos-1 in prev_positions]
                    if new_positions:
                        if doc not in new_documents_positions:
                            new_documents_positions[doc] = []
                        new_documents_positions[doc].extend(new_positions)
        documents_positions = new_documents_positions

    return list(documents_positions.keys())


# Assuming you have a list of preprocessed queries
queries = [
    "vintage",
]

print(positional_index)
# Execute queries
for query in queries:
    results = execute_phrase_query_without_preprocessing(query, positional_index)
    print(f"Query: {query}")
    print(f"Number of documents retrieved: {len(results)}")
    print(f"Documents: {', '.join(results)}\n")
