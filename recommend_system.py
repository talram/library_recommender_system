import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval


# books = pd.read_csv('name_books.csv', encoding='latin-1')
#
# books['isbn13'] = books['isbn13'].astype('int')
# books_tfidf = TfidfVectorizer(stop_words='english')
#
# books['title'] = books['title'].fillna('')
# book_title_matrix = books_tfidf.fit_transform(books['title'])
#
# similarity_matrix = cosine_similarity(book_title_matrix, book_title_matrix)
# 
# mapping = pd.Series(books.index, index=books['title'])


def recommend_book(book_input):
    book_index = mapping[book_input]

    # get similarity values with other books and similarity matrix
    similarity_score = list(enumerate(similarity_matrix[book_index]))

    # sort in descending order the similarity score of book inputted with all the other books
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # get the scores of the 5 most similar books. Ignore the first book.
    similarity_score = similarity_score[1:5]

    # return books ISBN13 using the mapping series
    book_indices = [i[0] for i in similarity_score]
    return books['isbn13'].iloc[book_indices]


