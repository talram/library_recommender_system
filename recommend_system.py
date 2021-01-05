import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Reading name_books file
books = pd.read_csv('name_books.csv', encoding='latin-1')

# Removing the stop words
books_tfidf = TfidfVectorizer(stop_words='english')

# Filling the missing values with empty string
books['title'] = books['title'].fillna('')

# Computing TF-IDF matrix required for calculating cosine similarity
book_title_matrix = books_tfidf.fit_transform(books['title'])


# Function to get the most similar books
def recommend_book(book_input):
    books_tfidf_vector = books_tfidf.transform([book_input])

    # Computing cosine similarity matrix
    similarity_matrix = cosine_similarity(books_tfidf_vector, book_title_matrix)

    # Get similarity values with other books and similarity matrix
    similarity_score = list(enumerate(similarity_matrix[0]))

    # Sort them in descending order
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # Get the scores of the top 3 most similar
    recommended_books = []
    for book_index in similarity_score:
        if len(recommended_books) == 3:
            break

        if books.iloc[book_index[0]]['title'] != book_input:
            recommended_books.append(book_index)

    # Return list of ISBN13s recommended books
    book_indices = [i[0] for i in recommended_books]
    return list(books.iloc[book_indices]['isbn13'])


