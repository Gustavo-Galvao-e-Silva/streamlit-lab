import streamlit as st
import pandas as pd

import info


def about_me_section():
    st.header("About Me")

    _, middle_column, _ = st.columns(3)
    with middle_column:
        st.image(info.profile_picture, width=250, caption="Here I am posing in front of Tech Tower on my first day on campus")

    st.write(info.about_me)
    st.write("---")

about_me_section()

# ======================================================

def links_section():
    st.sidebar.header("My Links")

    st.sidebar.text("Connect with me")
    linkedin_link = f"<a href='{info.my_linkedin_url}'><img src='{info.linkedin_image_url}' alt='LinkedIn' width = '75' height = '75'></a>"
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.text("Checkout my work")
    github_link = f"<a href='{info.my_github_url}'><img src='{info.github_image_url}' alt='LinkedIn' width = '75' height = '75'></a>"
    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    st.sidebar.text("Or shoot me an email")
    email_link = f"<a href='{info.my_email_address}'><img src='{info.email_image_url}' alt='LinkedIn' width = '75' height = '75'></a>"
    st.sidebar.markdown(email_link, unsafe_allow_html=True)

links_section()

# ======================================================

def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data["Institution"]}**")
    st.write(f"**Degree:** {education_data["Degree"]}")
    st.write(f"**Graduation Date:** {education_data["Graduation Date"]}")
    st.write(f"**GPA:** {education_data["GPA"]}")
    st.write("**Relevant coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(
        data=coursework,
        hide_index=True,
        column_config={
            "code": "Course Code",
            "name": "Course Name",
            "semester taken": "Semester Taken",
            "skills": "What I learned"
        }
    )
    st.write("---")

education_section(info.education_data, info.course_data)

# ======================================================

def experience_section(experience_data):
    st.header("Professional Experience")

    for title, (description, image) in experience_data.items():
        expander = st.expander(f"**{title}**")
        with expander:
            _, middle_column, _ = st.columns(3)
            with middle_column:
                st.image(image, width=250)
        for bullet_point in description:
            expander.write(bullet_point)

    st.write("---")

experience_section(info.experience_data)

# ======================================================

def project_section(project_data):
    st.header("Projects")

    for title, description in project_data.items():
        expander = st.expander(f"**{title}**")
        expander.write(description)
    st.write("---")

project_section(info.projects_data)

# ======================================================

def skills_section(programming_data, language_data):
    st.header("Skills")

    for language, percentage in programming_data.items():
        st.write(f"{language} {info.programming_icons.get(language, "")}")
        st.progress(percentage)

    for language, fluency in language_data.items():
        st.write(f"{language} {info.spoken_icons.get(language, "")}: {fluency}")

    st.write("---")

skills_section(info.programming_data, info.spoken_data)

# ======================================================

def activities_section(leadership_data, activity_data):
    st.header("Activities")

    tab_1, tab_2 = st.tabs(["Leadership", "Community Service"])
    with tab_1:
        st.subheader("Leadership")
        for title, (description, image) in leadership_data.items():
            expander = st.expander(f"**{title}**")
            with expander:
                _, middle_column, _ = st.columns(3)
                with middle_column:
                    st.image(image, width=250)
                for bullet_point in description:
                    expander.write(bullet_point)

    with tab_2:
        st.subheader("Community Service")
        for title, (description, image) in activity_data.items():
            expander = st.expander(f"**{title}**")
            with expander:
                _, middle_column, _ = st.columns(3)
                with middle_column:
                    st.image(image, width=250)
                for bullet_point in description:
                    expander.write(bullet_point)
    st.write("---")

activities_section(info.leadership_data, info.activity_data)