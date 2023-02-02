import streamlit as st

def about():
    #about page title
    st.title("Dataflix")
    
    about_dataflix, dataflix_logo, = st.columns([2, 1])
    
    with about_dataflix:
        st.write("**About the app**.")
        st.info("Dataflix is an application created for movie lovers. We are aware of the constant struggles of finding the right movie to" + 
                " watch. Dataflix is the unsung hero to all your problems. Dataflix is a movie recommendation application which uses " +
                "content-based and collaborative algorithms to recommend movies. Content-based filtering makes recommendation based on how" +
                " similar the properties or features of an item are to others. Collaborative filtering uses the similarity measured between" +
                " users to make recommendations.")
        st.markdown("")        
        #Meet the team 
        #st.write("**Meet the Team**.")
        st.image("resources/imgs/TeamJM2.png")


    
        st.markdown("")
    with dataflix_logo:
        st.image('resources/imgs/DATAFLIX(2).png', caption="© Dataflix")
