import streamlit as st


def intro_section():
    st.title("Web Development Lab01", width="content")
    st.header("CS 1301")
    st.subheader("Gustavo Galvao")


    st.write(
        """
            Welcome to my Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:
            
            1. My Portfolio: display of some projects, work experience, and my skills
            2. TF2 Quiz: find out which Team Fortress 2 character you are
        """
    )

intro_section()