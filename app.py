import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import random
import json

st.set_page_config(page_title="AI Interviewe Prep", layout="wide")

#read questions.json file

with open("questions.json", "r") as file:
    questions_bank = json.load(file)

st.sidebar.title("AI Interview Prep")

menu=st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Student Profile",
            "Skill Assessment",
            "Dashboard",
            "AI Roadmap",
            "Interview questions",
            "Progess Tracker"
        ]
    )


if 'scores' not in st.session_state:
    st.session_state.scores = 0


if 'student_Name' not in st.session_state:
    st.session_state.student_Name = ""


if 'role' not in st.session_state:
    st.session_state.role = ""

if menu == "Home":
    st.title("Welcome to AI Interview Prep")
    st.markdown("""
    ### Crack Technical Interviews with AI-Powerd Analysis
    Analyze your skills, detect weaknesses, genrate interview questions, and build a smart roadmap to ace your interviews.
    """) 

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", "100+")
col2.metric("Total Questions", "500+")
col3.metric("Success Rate", "87%")

st.divider()

st.subheader("What system can do")

col1, col2, = st.columns(2)

with col1:
    st.info("Skill Assessment: Evaluate your skills and identify areas for improvement.")
    st.info("weakness Detection: Detect your weaknesses and get personalized recommendations.")
    st.info("AI learning Roadmap")

with col2:
    st.info("Interview Question")
    st.info("Progress Tracking")
    st.info("AI readiness Prediction")


st.divider()

st.success("Start your journey to success with AI Interview Prep. Sign up now and take the first step towards acing your interviews!")

if menu == "Student Profile":
    st.title("Student Profile")
    name = st.text_input("Enter your name")

    role = st.selectbox("Select your role",
                        ["Data Scientist",
                         "Machine Learning Engineer",
                         "AI Researcher",
                         "AI Product Manager",
                         "Chandigarh University Professor"])

    branch = st.selectbox("Select your branch", ["BCA", "B.Tech", "M.Tech", "MCA", "PhD"])

    year = st.selectbox("Year of Study", ["1st Year", "2nd Year", "3rd Year", "4th Year", "5th Year"])

    if st.button("Save Profile"):
        st.session_state.student_Name = name
        st.session_state.role = role
        
        st.success("Profile saved successfully!")

elif menu == "Skill Assessment":
     
    st.title("Skill Assessment")

    st.markdown("Rate your skills on a scale of 1 to 5 (1 being the lowest and 5 being the highest) for the following AI-related topics:")

    arrays = st.slider("Arrays", 1, 5, 3)
    linked_lists = st.slider("Linked Lists", 1, 5, 3)
    stacks = st.slider("Stacks", 1, 5, 3)
    queues = st.slider("Queues", 1, 5, 3)
    dbms = st.slider("DBMS", 1, 5, 3)
    os = st.slider("Operating Systems", 1, 5, 3)

    if st.button("Analyse Skills"):

        st.session_state.scores = {
            "Arrays": arrays,
            "Linked Lists": linked_lists,
            "Stacks": stacks,
            "Queues": queues,
            "DBMS": dbms,
            "OS": os
        }

        st.success("Skills analysed successfully!")

elif menu == "Dashboard":
    st.title("Dashboard Analysis")
    
    if not st.session_state.scores:
        st.warning("Please complete the Skill Assessment first.")
    else:
        scores=st.session_state.scores

        df=pd.DataFrame({"Topic":list(scores.keys()),"Score":list(scores.values())})
        col1, col2, col3 = st.columns(3)
        avg_score=sum(scores.values())/len(scores)
        weak_topics=[topic for topic, score in scores.items() if score<3]
        strong_topics=[topic for topic, score in scores.items() if score>=3]
        
        col1.metric("Average Score", f"{avg_score:.2f}")
        col2.metric("Weak Topics", len(weak_topics))
        col3.metric("Strong Topics", len(strong_topics))
    
        st.subheader("Top performing Topics")
        fig,ax = plt.subplots(figsize=(5, 2.5))
        ax.bar(df["Topic"], df["Score"])
        plt.xticks(rotation=20)
        st.pyplot(fig)

        st.subheader("Weak Topics")
        if weak_topics:
            for topic in weak_topics:
                st.error(f"weak topic: {topic}")
        else:
            st.success("No weak topics found. Great job!")

        st.subheader("Strong Topics")
        for topic in strong_topics:
            st.success(f"Strong topic: {topic}")        
elif menu == "AI Roadmap":
    st.title("AI Roadmap")

    if not st.session_state.scores:
        st.warning("Please complete the Skill Assessment first.")
    else:
        scores = st.session_state.scores
        weak_topics = [topic for topic, score in scores.items() if score < 3]
    if not weak_topics:
        st.success("No weak topics found. Great job!")
    else:
        for topic in weak_topics:
            st.subheader(f"Recommended Resources for {topic} Roadmap")
            if topic == "Arrays":
                st.write("Week 1 :- Array Basics")
                st.write("Week 2 :- sliding Window Technique")
                st.write("Week 3 :- prefix Sum Technique")
                st.write("Week 4 :- Leetcode Problems")
            elif topic == "Linked Lists":
                st.write("Week 1 :- Linked List Basics")
                st.write("Week 2 :- Reverse Linked Lists")
                st.write("Week 3 :- Fast slow pointer")
                st.write("Week 4 :- Interview Problems")
            elif topic == "Stacks":
                st.write("Week 1 :- Stack Basics")
                st.write("Week 2 :- Monotonic Stack ")
                st.write("Week 3 :- Expression Evaluation")
                st.write("Week 4 :- Advanced Problems")
            elif topic == "Queues":
                st.write("Week 1 :- Queue Basics")
                st.write("Week 2 :- Circular Queue")
                st.write("Week 3 :- Priority Queue")    
                st.write("Week 4 :- Graph Applications")
            elif topic == "DBMS":
                st.write("Week 1 :- SQL Basics")
                st.write("Week 2 :- Joins")
                st.write("Week 3 :- Normalization")
                st.write("Week 4 :- Transactions and Indexing")
            elif topic == "OS":
                st.write("Week 1 :- Process Management")
                st.write("Week 2 :- Memory Management")
                st.write("Week 3 :- File Systems")
                st.write("Week 4 :- Concurrency and Synchronization")

elif menu == "Interview questions":
    st.title("Interview Questions")

    Topic = st.selectbox("Select a topic", 
                         list(questions_bank.keys()))
    
    difficulty = st.selectbox("Select difficulty level",
                              ["Easy", "Medium", "Hard"])
    if st.button("Generate Question"):
        question = random.sample(questions_bank[Topic],5)
        st.subheader(f"{difficulty} Level Questions")
         
        for i, q in enumerate(question, start=1):
            st.write(f"{i}.{q}")

elif menu == "Progess Tracker":
    st.title("Progress Tracker")
    
    if not st.session_state.scores:
        st.warning("Please complete the Skill Assessment first.")
    else:
        scores = st.session_state.scores
        progess_df = pd.DataFrame({
            'Topic': list(scores.keys()),
            'Current Score': list(scores.values()),
            'Target Score': [5] * len(scores)
        })

        st.dataframe(progess_df)

        st.subheader("Progress_df")
        avg_score = sum(scores.values()) / len(scores)

        X = [[1], [2], [3], [4], [5]]
        Y = ["Very Low", "Low", "Medium", "High", "Very High"]

        model = DecisionTreeClassifier()
        model.fit(X, Y)
        prediction = model.predict([[avg_score]])

        st.success(f"Your AI Readiness Level is: {prediction[0]}")
        if prediction[0] == "Very Low":
            st.error("You need to work hard to improve your skills.")
        elif prediction[0] == "Low":
            st.warning("You are on the right track, but there's room for improvement.")
        elif prediction[0] == "Medium":
            st.info("You have a decent understanding of AI concepts, but keep learning!")
        elif prediction[0] == "High":
            st.success("You have a strong grasp of AI concepts. Keep up the good work!")
        elif prediction[0] == "Very High":
            st.success("You are an AI expert! Keep pushing the boundaries of your knowledge!")  

 
                     
                            