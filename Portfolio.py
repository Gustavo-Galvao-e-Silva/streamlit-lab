import streamlit as st
import pandas as pd

import info

# Boilerplate classes
class Section:
    def __init__(self, header, content):
        self.header = header
        self.content = content


    def display_section(self):
        st.header(self.header)
        self.content()
        st.write("---")


class SidebarSection:
    def __init__(self, text, link, image, height, width, alt):
        self.text = text
        self.link = link
        self.image = image
        self.alt = alt
        self.height = height
        self.width = width

    def display_sidebar_section(self):
        with st.sidebar:
            col_1, col_2 = st.columns([2, 1])
            with col_1:
                st.write(self.text)

            with col_2:
                link = f"""
                <a href='{self.link}' target='_blank'>
                    <img src='{self.link}' alt='{self.alt}' width='{self.width}' height='{self.height}'>
                </a>
                """
                st.markdown(link, unsafe_allow_html=True)


# Content functions
def about_me_content(personal_data):
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(personal_data.profile_picture_path, width=200, caption="Me standing in front of the tech Tower in my first day on campus")

    st.write(personal_data.about_me)


def sidebar_content(personal_data, icons):
    st.sidebar.header("My Links")
    st.sidebar.header("")

    github_section = SidebarSection(
        text="A bit of my work : P",
        link=personal_data.github_url,
        image=icons.get("github"),
        height=50,
        width=50,
        alt="Github"
    )
    github_section.display_sidebar_section()

    linkedin_section = SidebarSection(
        text="Connect with me : )",
        link=personal_data.linkedin_url,
        image=icons.get("linkedin"),
        height=50,
        width=50,
        alt="LinkedIn"
    )
    linkedin_section.display_sidebar_section()

    email_section = SidebarSection(
        text="Shoot me an email ; )",
        link=personal_data.email_address,
        image=icons.get("email"),
        height=50,
        width=50,
        alt="Email"
    )
    email_section.display_sidebar_section()


def education_content(education_data, relevant_coursework_data):
    for education_entry in education_data:
        education_entry.display_education_content()

    st.subheader("Relevant Coursework")
    coursework = [course.get_course_dataframe() for course in relevant_coursework_data]
    coursework_dataframe = pd.concat(coursework)
    st.dataframe(
        coursework_dataframe,
        column_config={
            "code": "Course Code",
            "title": "Course Title",
            "institution": "Institution",
            "semester": "Semester Taken",
            "skills": "Skills",
        },
        hide_index=True
    )


# Section objects
about_me_section = Section(
    header="About me",
    content=lambda: about_me_content(info.personal_data)
)

education_section = Section(
    header="Education",
    content=lambda: education_content(info.education_data, info.relevant_courses_data)
)

# Section displaying
about_me_section.display_section()

sidebar_content(info.personal_data, info.icon_urls)

education_section.display_section()