"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Entity featurization and similarity computation
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Imported for our sanity
import warnings
warnings.filterwarnings('ignore')


# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',')
ratings = pd.read_csv('resources/data/ratings.csv')

movies_df = movies
#Drop duplicates 
movies_df = movies_df.drop(movies_df.loc[movies_df["title"].duplicated(keep='first') == True].index)



# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
   # Create a subset
    df=movies_df[:27000]
    
    # Data Preprocessing
    df['genres'] = df['genres'].str.replace('|', ' ')
    
    # Create a tfidf matrix and getting similarity indices
    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['genres'])
    tfidf_matrix.shape
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    df = df.reset_index()
    df=df.drop('index', axis=1)
    titles = df['title']
    indices = pd.Series(df.index, index=df['title'])

    #Movie 1
    idx_1 = indices[movie_list[0]]
    scores_1 = list(enumerate(cosine_sim[idx_1]))
    scores_1 = sorted(scores_1, key=lambda x: x[1], reverse=True)
   

    #Do the same for movie 2
    idx_2 = indices[movie_list[1]]
    scores_2 = list(enumerate(cosine_sim[idx_2]))
    scores_2 = sorted(scores_2, key=lambda x: x[1], reverse=True)
    

    #Do the same for movie 3
    idx_3 = indices[movie_list[2]]
    scores_3 = list(enumerate(cosine_sim[idx_3]))
    scores_3 = sorted(scores_3, key=lambda x: x[1], reverse=True)
    
    
    mix= scores_3 + scores_2 + scores_1
    mix=sorted(mix,key=lambda x: x[1],reverse=True)
    movie_indices = [i[0] for i in mix]
    recommended_movies=(titles.iloc[movie_indices])
    recommended_movies= [ elem for elem in recommended_movies if elem not in movie_list]
    recommended_movies= recommended_movies[0:top_n]
    return recommended_movies