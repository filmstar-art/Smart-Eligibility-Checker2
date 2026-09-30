
import streamlit as st

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #E8F0F7 !important;
}

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #17365D;
    text-align: center;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #526578;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Section headings */
.section-title {
    color: #17365D;
    font-size: 26px;
    font-weight: 600;
    margin-top: 20px;
}

/* Result card */
.result-card {
    background-color: #FFFFFF;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(23, 54, 93, 0.10);
    text-align: center;
    margin-top: 20px;
}

/* Score */
.score {
    font-size: 50px;
    font-weight: bold;
    color: #24527A;
}

/* Company card */
.company-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 10px rgba(23, 54, 93, 0.08);
}

/* Button */
.stButton > button {
    background-color: #24527A;
    color: #FFFFFF;
    border-radius: 8px;
    border: none;
    padding: 10px 25px;
    font-weight: 600;
}

/* Button hover */
.stButton > button:hover {
    background-color: #17365D;
    color: #FFFFFF;
}

/* Input boxes */
.stTextInput > div > div > input {
    background-color: #FFFFFF;
    border-radius: 8px;
}

/* Select boxes */
.stSelectbox > div > div {
    background-color: #FFFFFF;
    border-radius: 8px;
}

/* Multiselect */
.stMultiSelect > div > div {
    background-color: #FFFFFF;
    border-radius: 8px;
}

/* Divider */
hr {
    border: none;
    border-top: 1px solid #C8D6E3;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_icon="🎓",
    layout="wide"
)


st.markdown(
    '<div class="main-title">Smart Placement Eligibility Checker</div>',   
    unsafe_allow_html=True
)
st.markdown(
    '<div class ="subtitle">Check your placement eligibility and skill match.</div>',
    unsafe_allow_html=True
)



companies = [
    {
        "name": "Deloitte",
        "min_cgpa": 7.5,
        "max_backlogs": 0,
        "skills": ["Python", "Excel", "Communication", "Problem Solving"]
    },
    {
        "name": "EY",
        "min_cgpa": 7.0,
        "max_backlogs": 1,
        "skills": ["Excel", "Communication", "Analytical Thinking", "Python"]
    },
    {
        "name": "KPMG",
        "min_cgpa": 8.0,
        "max_backlogs": 0,
        "skills": ["Excel", "Python", "Communication", "Problem Solving"]
    },
    {
        "name": "TCS",
        "min_cgpa": 6.5,
        "max_backlogs": 2,
        "skills": ["Python", "Communication", "Problem Solving", "Logical Reasoning"]
    }
]

st.markdown(
    '<div class = "section-title">Student Profile</div>',
    unsafe_allow_html=True
)

col1,col2 = st.columns(2)
with col1:
 name = st.text_input("Enter your name:")
 college_name = st.text_input("Enter your college name:")
 course = st.text_input("Enter your course:")
 college_year = st.selectbox("Enter your college year :",['1st year', '2nd year', '3rd year', '4th year'])
 stream_name = st.selectbox("Enter your stream name:", ['Non-Medical', 'Medical', 'Commerce', 'Arts', 'Other'])

with col2:
 cgpa_input = st.number_input("Enter your CGPA (till now):", min_value=0.0, max_value=10.0, step=0.1)
 class_10 = st.number_input("Enter your 10th grade percentage:", min_value=0.0, max_value=100.0, step=0.1)
 class_12 = st.number_input("Enter your 12th grade percentage:", min_value=0.0, max_value=100.0, step=0.1)
 prefered_companies = st.multiselect(
     "Enter your prefered companies",
     ["Deloitte", "EY", "KPMG", "TCS"]
 )


st.markdown(
    '<div class = "section-title">Skills Assessment</div>',
    unsafe_allow_html=True
)
interests = st.text_input("Enter your interests (comma-separated):")
projects = st.text_input("Enter your projects completed till now (comma-separated):")

st.markdown(
    '<div class = "section-title"> Academic Details</div>',
    unsafe_allow_html=True
)
backlogs_input = st.number_input("Enter the number of backlogs:", min_value=0, max_value=10, step=1)

st.markdown(
    '<div class = "selection-title"> Your Skills</div>',
    unsafe_allow_html=True
)
aptitude = st.slider('Rate your Aptitude (1-10):', 1, 10, 5)
python_excell = st.slider('Rate your Python and Excel skills (1-10):', 1, 10, 5)
soft_skills = st.slider('Rate your Soft Skills (1-10):', 1, 10, 5)

skills_input = st.multiselect(
    "Enter the skills you currently have:",
    ["Python", "Java", "C++", "JavaScript", "Excel", "Communication"]
)

cgpa_score = (cgpa_input/10) * 30
class_10_score = (class_10/100) * 10
class_12_score = (class_12/100) * 10
aptitude_score = (aptitude/10) * 15
python_excell_score = (python_excell/10) * 15
soft_skills_score = (soft_skills/10) * 10

if projects.strip():
    project_score = 10
else:
    project_score = 0

eligibility_score = (
    cgpa_score
    + class_10_score
    + class_12_score
    + aptitude_score
    + python_excell_score
    + soft_skills_score
    + project_score
)

eligiblity_score = min(eligibility_score, 100)

if eligiblity_score >= 85:
    scale = "Excellent"
    message = "You are highly eligible for placements. Keep up the good work!"
elif eligiblity_score >= 70:
    scale = "Good"
    message = "You are eligible for placements. Focus on improving your skills and knowledge."
elif eligiblity_score >= 50:
    scale = "Average"
    message = "You have a fair chance of getting placed. Work on your skills and knowledge to improve your eligibility."
else:
    scale = "Poor"
    message = "You need to work hard to improve your eligibility for placements. Focus on academics and enhancing your skills and knowledge."

st.write("")
analyze = st.button('Analyze my placement profile', use_container_width=True)

if analyze:

    if cgpa_input == 0:
        st.warning("Please enter your CGPA to analyze your placement profile.")

    elif class_10 == 0 or class_12 == 0:
        st.warning("Please enter your 10th grade percentage to analyze your placement profile.")

    elif interests == None:
        st.warning("Please enter your interests")

    elif projects == None:
        st.warning("Please enter your projects that you have made till now")
    
    else:
        cgpa_score = (cgpa_input/10) * 30
        class_10_score = (class_10/100) * 10
        class_12_score = (class_12/100) * 10
        aptitude_score = (aptitude/10) * 15
        python_excell_score = (python_excell/10) * 15
        soft_skills_score = (soft_skills/10) * 10
    
        if projects.strip():
          project_score = 10
        else:
          project_score = 0

        eligibility_score = (
         cgpa_score
        + class_10_score
        + class_12_score
        + aptitude_score
        + python_excell_score
        + soft_skills_score
        + project_score
)
        eligiblity_score = min(eligibility_score, 100)

        if eligiblity_score >= 85:
            scale = "Excellent"
            message = "You are highly eligible for placements. Keep up the good work!"
        elif eligiblity_score >= 70:
            scale = "Good"
            message = "You are eligible for placements. Focus on improving your skills and knowledge."
        elif eligiblity_score >= 50:
            scale = "Average"
            message = "You have a fair chance of getting placed. Work on your skills and knowledge to improve your eligibility."
        else:
            scale = "Poor"
            message = "You need to work hard to improve your eligibility for placements. Focus on academics and enhancing your skills and knowledge."


        st.markdown(
            '<div class="selection-title">Placement Analysis</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="result-card">
                <div class="score">{score:.1f}/100</div>
                <h2>{scale}</h2>
                <p>{message}</p>
            </div>
            """.format(score=eligibility_score, scale=scale, message=message),
            unsafe_allow_html=True,
        )

        st.subheader('Score breakdown')
        score_col1, score_col2, score_col3, score_col4 = st.columns(4)
        with score_col1:
            st.metric('CGPA', f"{cgpa_score:.1f}/30")
        with score_col2:
            st.metric('Class 10', f"{class_10_score:.1f}/10")
        with score_col3:
            st.metric('Class 12', f"{class_12_score:.1f}/10")
        with score_col4:
            st.metric('Aptitude', f"{aptitude_score:.1f}/15")

        score_col5, score_col6, score_col7 = st.columns(3)
        with score_col5:
            st.metric('Excel and Python', f"{python_excell_score:.1f}/15")
        with score_col6:
            st.metric('Soft skills', f"{soft_skills_score:.1f}/10")
        with score_col7:
            st.metric('Projects', f"{project_score:.1f}/10")

        st.markdown('<div class="section_title">Company Eligibility</div>', unsafe_allow_html=True)

        eligible_companies = []
        for company in companies:
            if (
                cgpa_input >= company["min_cgpa"]
                and backlogs_input <= company["max_backlogs"]
            ):
                eligible_companies.append(company)
        if eligible_companies:
            st.success('You meet the basic eligibility criteria')

        for company in eligible_companies:
            company_name = company['name']
            required_skills = company['skills']
            matching_skills = []
            missing_skills = []
            for skill in required_skills:
                if skill in skills_input:
                    matching_skills.append(skill)
                else:
                    missing_skills.append(skill)

            if len(required_skills) > 0:
                match_percentage = (len(matching_skills)/len(required_skills))*100
            else:
                match_percentage = 0 

            st.markdown(
                f"""
                <div class = "Company-Card">
                   <h2> {company_name} </h2>
                   <p> 
                   <b> Minimum CGPA: </b>
                   {company["min_cgpa"]}
                   </p>

                   <p>
                   <b> Maximum Backlogs: </b>
                   {company["max_backlogs"]}
                   </p>

                   <p>
                   <b> Skill Match: </b>
                   {match_percentage:0.0f}%
                   </p>
                </div>
                """,
                unsafe_allow_html=True

            ) 

            if matching_skills:
               
                    st.write(
                        "✅ **Matching Skills:** "
                        + ", ".join(matching_skills)
                    )

            if missing_skills:

                    st.write(
                        "⚠️ **Skills to Improve:** "
                        + ", ".join(missing_skills)
                    )

            st.divider()
        else:
    
                st.warning(
                    "No companies currently match your basic CGPA "
                    "and backlog requirements."
                )
    
        if prefered_companies:
        
                    st.markdown(
                        '<div class="section-title">⭐ Preferred Company Analysis</div>',
                        unsafe_allow_html=True
                    )
        
                    for preferred in prefered_companies:
        
                        company_found = None
        
                        for company in companies:
        
                            if company["name"] == preferred:
        
                                company_found = company
                                break
        
        
                        if company_found:
        
                            required_skills = company_found["skills"]
        
                            matching_skills = []
        
                            missing_skills = []
        
                            for skill in required_skills:
        
                                if skill in skills_input:
        
                                    matching_skills.append(skill)
        
                                else:
        
                                    missing_skills.append(skill)
        
        
                            if len(required_skills) > 0:
        
                                preferred_match = (
                                    len(matching_skills)
                                    / len(required_skills)
                                ) * 100
        
                            else:
        
                                preferred_match = 0
        
        
                            st.subheader(
                                f"🎯 {preferred}"
                            )
        
                            if (
                                cgpa_input >= company_found["min_cgpa"]
                                and backlogs_input <= company_found["max_backlogs"]
                            ):
        
                                st.success(
                                    "You meet the basic academic eligibility."
                                )
        
                            else:
        
                                st.error(
                                    "You currently do not meet the basic "
                                    "academic eligibility."
                                )
        
        
                            st.progress(
                                int(preferred_match)
                            )
        
                            st.write(
                                f"**Skill Match: {preferred_match:.0f}%**"
                            )
        
                            if matching_skills:
        
                                st.write(
                                    "✅ Matching: "
                                    + ", ".join(matching_skills)
                                )
        
                            if missing_skills:
        
                                st.write(
                                    "⚠️ Improve: "
                                    + ", ".join(missing_skills)
                                )

        st.markdown(
                    '<div class="section-title">🚀 Skills Improvement Plan</div>',
                    unsafe_allow_html=True
                )
        
        improvement_needed = []
        
        if aptitude < 6:
        
                    improvement_needed.append(
                        "Aptitude & Reasoning"
                    )
        
        if python_excell < 6:
        
                    improvement_needed.append(
                        "Excel & Python"
                    )
        
        if soft_skills < 6:
        
                    improvement_needed.append(
                        "Soft Skills & Communication"
                    )
        
        if not projects.strip():
        
                    improvement_needed.append(
                        "Projects"
                    )
        
        if improvement_needed:
        
                    st.warning(
                        "Focus on improving: "
                        + ", ".join(improvement_needed)
                    )
        
        else:
        
                    st.success(
                        "Your self-rated skill profile is strong. "
                        "Keep developing these skills."
                    )


        st.markdown(
                    '<div class="section-title">📋 Profile Summary</div>',
                    unsafe_allow_html=True
                )
        
        summary_col1, summary_col2 = st.columns(2)
        
        with summary_col1:
        
                    st.write(
                        f"**Project:** {projects if projects else 'Not provided'}"
                    )
        
                    st.write(
                        f"**College:** {college_name if college_name else 'Not provided'}"
                    )
        
                    st.write(
                        f"**Year:** {college_year}"
                    )
        
                    st.write(
                        f"**Stream:** {stream_name if stream_name else 'Not provided'}"
                    )
        
        with summary_col2:
        
                    st.write(
                        f"**CGPA:** {cgpa_input}"
                    )
        
                    st.write(
                        f"**Class 10:** {class_10}%"
                    )
        
                    st.write(
                        f"**Class 12:** {class_12}%"
                    )
        
                    st.write(
                        f"**Interests:** {interests if interests else 'Not provided'}"
                    )
        
st.write("")

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#6c757d;">
        🎓 Smart Placement Assistant |
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)   