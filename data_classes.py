import pandas as pd
import streamlit as st


class PersonalData:
    def __init__(self, about_me, profile_picture_path, linkedin_url, github_url, email_address):
        self.about_me = about_me
        self.profile_picture_path = profile_picture_path
        self.linkedin_url = linkedin_url
        self.github_url = github_url
        self.email_address = email_address


class EducationData:
    def __init__(self, degree, institution, location, start_date, end_date, gpa="N/A"):
        self.degree = degree
        self.institution = institution
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.gpa = gpa

    def display_education_content(self):
        st.subheader(f"**{self.institution}**")
        st.write(f"{self.location} | {self.start_date} - {self.end_date}")
        st.write(f"**Degree**: {self.degree}")
        st.write(f"**GPA**: {self.gpa}")


class CourseData:
    def __init__(self, code, name, institution, semester_taken, skills):
        self.code = code
        self.name = name
        self.institution = institution
        self.semester_taken = semester_taken
        self.skills = skills


    def get_course_dataframe(self):
        return pd.DataFrame({
            "code":[self.code],
            "name": [self.name],
            "institution": [self.institution],
            "semester": [self.semester_taken],
            "skills": [self.skills],
        })


class WorkExperienceData:
    def __init__(self, icon, position, employer, location, description_points, image_path):
        self.icon = icon
        self.position = position
        self.employer = employer
        self.location = location
        self.description_points = description_points
        self.image_path = image_path


class ProjectData:
    def __init__(self, title, relevant_skills, start_date, end_date, description_points, image_path, links):
        self.title = title
        self.relevant_skills = relevant_skills
        self.start_date = start_date
        self.end_date = end_date
        self.description_points = description_points
        self.image_path = image_path
        self.links = links


class LanguageData:
    def __init__(self, name, icon, proficiency):
        self.name = name
        self.icon = icon
        self.proficiency = proficiency