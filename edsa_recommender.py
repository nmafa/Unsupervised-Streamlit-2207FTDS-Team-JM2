"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import hydralit_components as hc


# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import time
import resources.functions.trailers as t 
import nav_bar.about as a
import nav_bar.contact as c
import nav_bar.help as h
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

#Page Config
st.set_page_config(page_icon='resources/imgs/DATAFLIX.png', page_title= 'Dataflix', layout='wide', initial_sidebar_state='auto')

over_theme = {'txc_inactive': '#FFFFFF'}

# specify the primary menu definition
menu_data = [
    {'icon': "fa fa-users", 'label':'About Us'},
    {'id':'Contact Us','icon': 'fa fa-envelope', 'label':'Contact Us'},
    {'id':'Help', 'icon': 'fa fa-question-circle', 'label':'Help'}
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    #login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)
page_selection = f'{menu_id}'

# App declaration
def main():

    

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    #page_options = ["Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    #page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Home":
        # Header contents
        st.write('# DATAFLIX')
        #st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    #Hydralit loaders
                    with hc.HyLoader('Your TOP 10 recommendations are...',hc.Loaders.standard_loaders,index=[3,0,5]):
                        top_recommendations = content_model(movie_list=fav_movies,top_n=10)
                        time.sleep(5)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        #get youtube trailer 
                        t.trailers(top_recommendations[i])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    #Hydralit loaders
                    with hc.HyLoader('Your TOP 10 recommendation are...',hc.Loaders.standard_loaders,index=[3,0,5]):
                        top_recommendations = collab_model(movie_list=fav_movies,top_n=10)
                        time.sleep(5)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        #get youtube trailer 
                        t.trailers(top_recommendations[i])
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    elif page_selection == 'About Us':
        # navigate to the About page
        a.about()
    elif page_selection == 'Contact Us':
        # navigate to the Contact Us page
        c.contact_us()
    elif page_selection == 'Help':
        # navigate to the Help page
        h.help()
  
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
