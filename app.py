import streamlit as st
from groq import Groq

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.title("StudyAI Helper - AI Study Assistant")
st.subheader("Paste your lecture notes → Generate summary + review questions → Answer and get feedback!")


text = st.text_area("Paste your notes/text here (e.g., lecture summary, article):", height=250)


if 'ai_result' not in st.session_state:
    st.session_state.ai_result = None
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = [""] * 5
if 'feedback' not in st.session_state:
    st.session_state.feedback = None


if st.button("Generate Summary & Questions") and text:
    with st.spinner("Processing with AI..."):
        generate_prompt = f"""
        You are an excellent study assistant.
        Provided text: {text}

        In English, do the following:
        1. Create a concise summary (max 150 words).
        2. Generate exactly 5 review questions based on the text (mix multiple-choice and open-ended; number them 1 to 5).
        Format nicely with markdown: use ## for headings, - for lists, etc.
        Separate the summary from questions with a clear line like '--- Review Questions ---'.
        """

        try:
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a smart and helpful tutor."},
                    {"role": "user", "content": generate_prompt},
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=1000,
            )
            st.session_state.ai_result = response.choices[0].message.content
            st.session_state.feedback = None 

            lines = st.session_state.ai_result.split('\n')
            questions = []
            for line in lines:
                if line.strip().startswith(('1.', '2.', '3.', '4.', '5.')):
                    questions.append(line.strip())
            st.session_state.questions = questions[:5]

        except Exception as e:
            st.error(f"API error: {e}. Check your API key, connection, or try again.")

if st.session_state.ai_result:
    st.markdown("### AI Result:")
    st.markdown(st.session_state.ai_result)

    st.markdown("### Now answer the questions below:")
    for i in range(5):
        if i < len(st.session_state.questions):
            st.subheader(f"Question {i+1}:")
            st.markdown(st.session_state.questions[i])
            st.session_state.user_answers[i] = st.text_area(
                f"Your answer to Question {i+1}:",
                value=st.session_state.user_answers[i],
                height=100,
                key=f"ans_{i}"
            )

    if st.button("Check My Answers"):
        with st.spinner("Grading with AI..."):
            answers_str = "\n".join([f"Question {i+1}: {q}\nStudent's answer: {a}" for i, (q, a) in enumerate(zip(st.session_state.questions, st.session_state.user_answers))])

            verify_prompt = f"""
            You are a strict but fair teacher grader.
            Original lecture text (for reference): {text[:2000]}... (truncated content)

            Evaluate each of the 5 student answers:
            - Say if it's Correct, Partial, or Incorrect.
            - Give a short explanation (1-3 sentences).
            - Assign a score from 0 to 10 for each.
            - At the end, give an overall average score and motivational feedback.

            Student's answers:
            {answers_str}

            Format nicely in markdown: use numbered lists or a table.
            """

            try:
                response_verify = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a precise grading tutor."},
                        {"role": "user", "content": verify_prompt},
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.6,
                    max_tokens=1200,
                )
                st.session_state.feedback = response_verify.choices[0].message.content
            except Exception as e:
                st.error(f"Verification error: {e}")

    if st.session_state.feedback:
        st.markdown("### AI Grading & Feedback:")
        st.markdown(st.session_state.feedback)
