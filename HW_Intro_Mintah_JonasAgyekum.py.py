#%%
from IPython.display import Markdown, display

markdown_content = """

My name is Jonas Agyekum Mintah, and I'm currently pursuing a Master of Science in Statistics with a concentration in Applied Probability and Statistical Modeling at the George Washington University. My academic interests include statistical analysis, linear models, and probability. I enjoy solving complex problems and applying statistical concepts to real-world scenarios.

In my free time, I like to explore educational platforms that make learning accessible to everyone. One of my favorite websites is (https://www.datacamp.com), which offers free courses on a variety of subjects. I believe in the power of education and technology to transform lives and am passionate about contributing to this field.
"""
display(Markdown(markdown_content))
#%%


# %%
myCourseTitles = [
  "Intro to Data Science",
    "Intro to Machine Learning",
    "Data Warehousing",
    "Intro to Data Mining",
    "Time Series Analysis",
    "Deep Learning"
  ]
print(myCourseTitles[-1])
#%%


#%%
myCourseTitles[3] = "Intro to Coal Mining"
#%%


# %%
myCourseList = {
    "DATS 6101": "Intro to Data Science",
    "DATS 6202": "Intro to Machine Learning",
    "DATS 6102": "Data Warehousing",
    "N/A": "Intro to Coal Mining",
    "DATS 6313": "Time Series Analysis",
    "DATS 6304": "Deep Learning"
}
# %%

#%%
number_of_classes = len(myCourseList)
print(number_of_classes)
# %%


# %%
myTupleCourseTitles = tuple(myCourseTitles)
half_index = len(myTupleCourseTitles) // 2  
print(myTupleCourseTitles[half_index:])
# %%


# %%
myself = {
    "Firstname": "Jonas Agyekum",
    "Lastname": "Mintah",
    "CompletedClasses": [
        {
            "CourseNumber": "DATS 6101",
            "CourseTitle": "Intro to Data Science",
            "Prerequisites": [],
            "Year": 2024,
            "Semester": "Fall",
            "Instructor": "Dr. Darcy Morris"
        },
        {
            "CourseNumber": "DATS 6202",
            "CourseTitle": "Intro to Machine Learning",
            "Prerequisites": [
                {
                    "CourseNumber": "DATS 6101",
                    "CourseTitle": "Intro to Data Science",
                    "Prerequisites": [],
                }
            ],
            "Year": 2024,
            "Semester": "Fall",
            "Instructor": "Dr. Yuxiao Huang"
        },
    ],
    "InProgressClasses": [
        {
            "CourseNumber": "DATS 6103",
            "CourseTitle": " Intro to Data Mining",
            "Prerequisites": [],
            "Year": 2025,
            "Semester": "Spring",
            "Instructor": "Dr. Ning Rui"
        },
       {
            "CourseNumber": "DATS 6102",
            "CourseTitle": " Data Warehousing",
            "Prerequisites": [],
            "Year": 2025,
            "Semester": "Spring",
            "Instructor": "Dr. Hazim Shatnawi"
        },  
    ],
    "PlannedClasses": [
        {
            "CourseNumber": "DATS 6313",
            "CourseTitle": "Time Series Analysis",
            "Prerequisites": [
                {
                    "CourseNumber": "DS101",
                    "CourseTitle": "Introduction to Data Science",
                    "Prerequisites": []
                },
            ]
        },
        {
            "CourseNumber": "DATS 6304",
            "CourseTitle": "Deep Learning",
            "Prerequisites": [
                {
                    "CourseNumber": "DATS 6202",
                    "CourseTitle": "Intro to Machine Learning",
                    "Prerequisites": [
                        {
                            "CourseNumber": "DATS 6101",
                            "CourseTitle": "Introduction to Data Science",
                            "Prerequisites": []
                        }
                    ]
                }
            ]
        }
    ],
    "ExpectedGraduationYear": 2026
}
# %%
print(myself)
#%%

#%%
 
import copy

friend_info = copy.deepcopy(myself)
#%%
friend_info["Firstname"] = "George"
friend_info["Lastname"] = "Smith"
friend_info["ExpectedGraduationYear"] = 2026
print( myself)
print(friend_info)
# %%
 
