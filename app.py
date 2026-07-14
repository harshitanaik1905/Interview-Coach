import streamlit as st
from interview_questions import questions
from llm_analysis import evaluate_answer
from feedback_engine import generate_feedback
from scoring import calculate_score

st.markdown("""
<style>
.main-title{
    font-size:42px;
    font-weight:bold;
    color:#1E3A8A;
}
.subtitle{
    font-size:18px;
    color:#6B7280;
    margin-bottom:20px;
}
.card{
    background-color:#F8FAFC;
    padding:25px;
    border-radius:12px;
    border:1px solid #D1D5DB;
}
hr{
    margin-top:25px;
    margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "role" not in st.session_state:
    st.session_state.role = ""
if "company" not in st.session_state:
    st.session_state.company = ""
if "difficulty" not in st.session_state:
    st.session_state.difficulty = ""
if "interview_type" not in st.session_state:
    st.session_state.interview_type = ""
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "ai_score" not in st.session_state:
    st.session_state.ai_score = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = {}
if "score_card" not in st.session_state:
    st.session_state.score_card = {}

st.sidebar.title("AI Interview Coach")
selected_page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Interview",
        "Reports",
        "Settings"
    ]
)
if selected_page == "Home":
    st.markdown(
        '<p class="main-title">AI Interview Coach</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="subtitle">Practice interviews with AI-powered feedback.</p>',
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.subheader("Interview Configuration")
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox(
            "Job Role",
            [
                "AI/ML Intern",
                "Python Developer",
                "Data Analyst",
                "Web Developer",
                "Software Engineer"
            ]
        )
        difficulty = st.selectbox(
            "Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        )
    with col2:
        interview_type = st.selectbox(
            "Interview Type",
            [
                "Technical",
                "HR",
                "Behavioral"
            ]
        )
        company = st.selectbox(
            "Target Company",
            [
                "Google",
                "Microsoft",
                "Amazon",
                "Infosys",
                "TCS",
                "Accenture"
            ]
        )
    st.markdown("---")
    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )
    if uploaded_resume is not None:
        st.success(
            f"Uploaded: {uploaded_resume.name}"
        )
    st.markdown("---")
    if st.button(
        "Start Interview",
        use_container_width=True
    ):
        
        st.session_state.role = role
        st.session_state.company = company
        st.session_state.difficulty = difficulty
        st.session_state.interview_type = interview_type

        question_list = questions[role][difficulty]
        st.session_state.current_question = question_list[0]
        st.session_state.question_index = 0

        st.success("Interview configuration saved successfully.")

elif selected_page == "Interview":
    st.title("Interview")
    if st.session_state.role == "":
        st.warning("Please configure your interview from the Home page.")
    else:
        st.write("### Interview Details")
        st.write("**Job Role:**", st.session_state.role)
        st.write("**Interview Type:**", st.session_state.interview_type)
        st.write("**Difficulty:**", st.session_state.difficulty)
        st.write("**Target Company:**", st.session_state.company)

        st.markdown("---")
        st.subheader(f"Question {st.session_state.question_index + 1}")
        st.info(st.session_state.current_question)

        answer = st.text_area(
            "Type your answer here"
        )
        col1, col2 = st.columns(2)
        with col1:
          if st.button("Submit Answer"):
            if answer.strip() == "":
                st.error("Please enter your answer.")
            else:
                expected_answer = st.session_state.current_question
                result = evaluate_answer(
                  st.session_state.current_question,
                  expected_answer,
                  answer )
                st.session_state.ai_score = result["score"]
                st.session_state.feedback = generate_feedback(
                result["score"]
                 )
                st.session_state.score_card = calculate_score(
                result["score"]
                 )
                st.success("Answer evaluated successfully.")
        with col2:

           if st.button("Next Question"):
              question_list = questions[
              st.session_state.role
              ][
             st.session_state.difficulty
             ]
              if st.session_state.question_index < len(question_list) - 1:
               st.session_state.question_index += 1
               st.session_state.current_question = question_list[
                    st.session_state.question_index
               ]
               st.rerun()
              else:
                st.success("Interview Completed.")
if st.session_state.score_card:
    st.markdown("---")
    st.subheader("AI Evaluation")
    st.write("### Score")
    st.write(
        f"Overall Score: {st.session_state.score_card['Overall']}%"
    )
    st.write(
        f"Technical: {st.session_state.score_card['Technical']}%"
    )
    st.write(
        f"Communication: {st.session_state.score_card['Communication']}%"
    )
    st.write(
        f"Confidence: {st.session_state.score_card['Confidence']}%"
    )
    st.write(
        f"Grammar: {st.session_state.score_card['Grammar']}%"
    )
    st.markdown("---")
    st.subheader("Performance")
    st.success(
        st.session_state.feedback["performance"]
    )
    st.write("### Strengths")
    for item in st.session_state.feedback["strengths"]:
        st.write("-", item)
    st.write("### Improvements")
    for item in st.session_state.feedback["improvements"]:
        st.write("-", item)    

elif selected_page == "Reports":
    st.title("Reports")
    st.info(
        "Interview reports will be available after completing an interview."
    )

elif selected_page == "Settings":
    st.title("Settings")
    st.subheader("Interview Settings")
    if st.button("Reset Interview"):
        st.session_state.role = ""
        st.session_state.company = ""
        st.session_state.difficulty = ""
        st.session_state.interview_type = ""
        st.success("Interview configuration has been reset.")
