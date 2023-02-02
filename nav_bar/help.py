import streamlit as st

def help():
    st.title("Not sure on how the app works?")
    st.write("choose a drop down below")

    with st.expander("Home"):
        #Create the help section for home page. 
        #st.title("Home")
        #create Steps for the Home page.
        st.title("Follow the steps below")
        st.write("Choose Between Content based or Collaborative based filtering.")
        
        st.info(
            """
        - Content-based filtering uses a series of discrete characteristics of your selected movies in order to recommend additional movies with similar properties.

        
        - Collaborative filtering checks on your past behaviour or similar decisions made by other users.


        - For this app, the best filtering method is the collaborative filter. This recommender uses user ratings to find similarity between the movies users select and those that they have not watched yet. It allows users discover new interests. In isolation, a Machine Learning model may not know the user is interested in a given movie, but this model might still recommend it because similar movie was rated the same by other users. The collaborative filtering model runs faster, preventing users from running out of patience and data
        
        """
        )
        st.markdown("To understand how recommender systems work and why they are important, Please check the video bellow.")
        if st.checkbox('View video'): # data is hidden if box is unchecked
            st.video('https://www.youtube.com/watch?v=Eeg1DEeWUjA&feature=youtu.be&ab_channel=CS50')
        
        
        st.write(
            """
        - Select your 1st, 2nd & 3rd favourite movie.
        - Press the Recommend button.
        - Enjoy the selection of recommended films and their trailers.
        """
                )
    
    #create the About help section.
    with st.expander("About Us"):

    #create the Step by step guide for the About Page.
        st.title("Follow the Steps")
        st.write(
            """
        - Find out about Dataflix.
        - Get a glimpse of the team behind the amazing work.
        - See our cool logo
        """
        )
    
    
        
    #create the Contact Us help section.
    with st.expander("Contact Us"):


    
    #create the Step by step guide for the Contact Us Page.
        st.title("Follow these Steps")
        st.write(
            """
            The contact us page is pretty simple and straight forward incase you want to halla at us.
            
            - Add your name.
            - Add your email.
            - Leave your message or concerns and we will get back to you.
     
        
            """
                )