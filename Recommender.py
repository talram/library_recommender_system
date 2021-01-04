import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import json



##urls from the server
#books_to_recommend =
#title =
#need to import a json via request and then enter it to new data dictionary
#a dictionary from the shelf for recommendation process
#new_data = {
 #   books_to_recommend: {
  #      "user_id": user,
   #     "b_title": title
   # }
#}
# reading file
book_title = pd.read_csv('list_of_titles.csv', encoding='latin-1')
dataset = pd.read_csv('books.csv', encoding='latin-1')

# removing the stop words
books_tfidf = TfidfVectorizer(stop_words='english')

# filling the missing values with empty string
#book_title['title'] = book_title['title'].fillna('')

# computing TF-IDF matrix required for calculating cosine similarity
book_title_matrix = books_tfidf.fit_transform(book_title['title'])

# computing cosine similarity matrix using linear_kernal of sklearn
cosine_similarity = linear_kernel(book_title_matrix, book_title_matrix)
indices = pd.Series(book_title['isbn13'].index)


# function to get the most similar books

##title instead index
def recommend(index, cosine_sim=cosine_similarity):
    id = indices[index]
    # Get the pairwise similarity scores of all books compared to that book,
    # sorting them and getting top 4
    similarity_scores = list(enumerate(cosine_sim[id]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:5]

    # Get the books index
    books_index = [i[0] for i in similarity_scores]

    # Return isbn13 of the top 5 most similar books using integer-location based indexing (iloc)
    # Need to return this as a json file format.
    return book_title['isbn13'].iloc[books_index]

    # getting recommendation for book at index 2


    # recommend to the shelf
    # read the json from the shelf
    # and then update and write to a new dictionary

     ##Finally to delete the entry if necessary
    #finally:   shelf_entry.delete(0,END)

    ##POST to URL

