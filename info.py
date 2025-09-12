from data_classes import EducationData, CourseData, WorkExperienceData, PersonalData, LanguageData, ProjectData

icon_urls = {
    "linkedin": "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg",
    "github": "https://cdn-icons-png.flaticon.com/256/25/25231.png",
    "email": "https://logowik.com/content/uploads/images/513_email.jpg"
}


personal_data = PersonalData(
    about_me="Hey there! I am Gustavo, but you can call me Gus - or Guga. I am a Computer Science Sophomore at Georgia Tech, and previously interned for iFood as a Machine Learning Engineer",
    profile_picture_path="Images/profile.jpg",
    linkedin_url="https://www.linkedin.com/in/gustavo-galvao-e-silva-125884209/",
    github_url="https://github.com/Gustavo-Galvao-e-Silva",
    email_address="gustavo.galvaoesilva@gmail.com",
)


education_data = [
    EducationData(
        degree="Bachelor of Science in Computer Science",
        institution="Georgia Institute of Technology",
        location="Atlanta, GA",
        start_date="Aug. 2025",
        end_date="May 2028"
    ),
    EducationData(
        degree="Bachelor of Science in Computer Science",
        institution="University of South Florida",
        location="Tampa, FL",
        start_date="Aug. 2023",
        end_date="May 2025",
        gpa="4.0"
    )
]

relevant_courses_data = [
    CourseData(
        code="CS 1301",
        name="Intro to CS",
        semester_taken="Fall 2025",
        institution="Georgia Tech",
        skills="Python (GOAT 🐐 programming language)"
    ),
    CourseData(
        code="CS 2050",
        name="Discrete Mathematics",
        semester_taken="Fall 2025",
        institution="Georgia Tech",
        skills="Building proofs on why odd + even = odd"
    ),
    CourseData(
        code="COP 4500",
        name="Data Structures",
        semester_taken="Spring 2025",
        institution="USF",
        skills="Wrote C++ to create some nifty data structures (take a peek at it on my GitHub!)"
    ),
    CourseData(
        code="COP 3514",
        name="Program Design",
        semester_taken="Fall 2024",
        institution="USF",
        skills="Learned about C, memory management, code optimizations and data structures"
    )
]

work_experiences_data = [
    WorkExperienceData(
        icon= "💻",
        position= "Machine Learning Intern",
        employer="iFood",
        location="Hybrid, Brazil",
        description_points= [
            "-Developed and deployed ML models for chatbots for optimizing response selection with 80% accuracy to improve user engagement using BERT transformers and SciKit Learn models",
            "-Led the development of a semantic search and summarization platform with LLMs and Qdrant, cutting data extraction time by over 60% and lookup by 90%",
            "-Engineered scalable Databricks and Pandas pipelines for data ingestion and processing, text embedding, and AWS SageMaker training/deployment, enabling low-latency inference and building a scalable microsservice architecture"
        ],
        image_path="Images/ifood.jpg",
    ),
    WorkExperienceData(
        icon="🧮",
        position="Calculus II Peer Tutor",
        employer="University of South Florida",
        location="Tampa, FL",
        description_points= [
            "-Conducted weekly sessions for new engineering students, teaching them Calculus II concepts, improving their comprehension and achieving a satisfaction rating of over 9/10",
            "-Held weekly 1:1 tutoring office hours, boosting student performance and achieving one of the highest attendances of all tutors",
            "-Fostered a supportive learning environment, increasing attendance, participation, and community engagement"
        ],
        image_path="Images/ifood.jpg",
    )
]

project_data = ProjectData(
    title="HackUSF Website",
    relevant_skills=[
        "JavaScript",
        "React",
        "Next.js",
        "Firebase"
    ],
    start_date= "Feb. 2025",
    end_date= "Apr. 2025",
    description_points= [
        "-Website for my old club's (GDSC) hackathon. Some of its capabilities include the application page, participant profile, participant management, and event admin dashboard",
        "-I mainly worked on developing the admin dashboard. It manages participant check-in and ID generation, allocated meals, and automated Discord announcements. These functionalities **reduced operational overhead by almost 10-fold**",
        "-Also helped with the backend, cutting the API call times by **almost 80% and database reads by almost 10-fold**"
    ],
    image_path="Images/hackusf.jpg",
    links= {
        "Website": "https://hackusf.com",
        "Github Repo": "https://github.com/Gustavo-Galvao-e-Silva/HackUSF-Updated",
    }
)


programming_languages_data = [
    LanguageData(
        name="Python",
        icon="🐍",
        proficiency=90
    ),
    LanguageData(
        name="JavaScript/Typescript",
        icon="🕸️",
        proficiency=60
    )
]

spoken_language_data = [
    LanguageData(
        name="English",
        icon="🇬🇧",
        proficiency="Fluent"
    ),
    LanguageData(
        name="Portuguese",
        icon="🇵🇹",
        proficiency="Native"
    )
]
