import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

books = pd.read_csv('name_books.csv', encoding='latin-1')

books_tfidf = TfidfVectorizer(stop_words='english')

books['title'] = books['title'].fillna('')
book_title_matrix = books_tfidf.fit_transform(books['title'])


def recommend_book(book_input):
    books_tfidf_vector = books_tfidf.transform([book_input])

    similarity_matrix = cosine_similarity(books_tfidf_vector, book_title_matrix)

    # get similarity values with other books and similarity matrix
    similarity_score = list(enumerate(similarity_matrix[0]))

    # sort in descending order the similarity score of book inputted with all the other books
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # get the scores of the 3 most similar books. Ignore the same book.
    recommended_books = []
    for book_index in similarity_score:
        if len(recommended_books) == 3:
            break

        if books.iloc[book_index[0]]['title'] != book_input:
            recommended_books.append(book_index)

    # return books ISBN13 using the mapping series
    book_indices = [i[0] for i in recommended_books]
    return list(books.iloc[book_indices]['isbn13'])


