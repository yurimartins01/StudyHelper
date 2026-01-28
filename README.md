# StudyAI Helper

**AI-Powered Study Assistant for Students**  
Built for **AI for Bharat 2026: Year in Review, Code for Tomorrow** hackathon (Track: AI for Learning & Academics / Productivity).

### Problem
University students often struggle with summarizing long lecture notes, creating effective review questions, and self-testing their understanding — leading to procrastination, poor retention, and stress during exams.

### Solution
StudyAI Helper is a simple, interactive web app that uses fast AI (via Groq API) to:
- Generate concise summaries from pasted notes/text.
- Create 5 mixed review questions (multiple-choice + open-ended).
- Allow users to answer the questions.
- Automatically grade answers with feedback, explanations, and scores (0-10) using AI.

This makes studying more efficient, interactive, and accessible — especially for students in low-bandwidth or resource-limited environments (India-first focus on everyday student challenges).

### Features
- Paste any lecture notes/article → AI generates summary + questions.
- Answer questions directly in the app.
- One-click AI grading with detailed feedback and motivational notes.
- Clean, intuitive Streamlit UI.
- Fast inference with Groq's Llama models.

### Tech Stack
- **Frontend/UI**: Streamlit
- **AI Backend**: Groq API (Llama-3.3-70b-versatile for high-quality reasoning)
- **Language**: Python

### How to Run Locally
1. Clone the repo: `git clone https://github.com/SEU-USUARIO/study-ai-helper.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up secrets: Create `.streamlit/secrets.toml` with `GROQ_API_KEY = "your-key-here"` (get key at https://console.groq.com/keys)
4. Run: `python -m streamlit run app.py`

**Note**: API key is loaded securely via Streamlit secrets (never hardcoded or committed).

### Demo Video
[Link to your YouTube/Loom video here] (2-3 min demo showing full flow)

### Impact
Helps students save time on note review, improve self-assessment, reduce exam anxiety, and boost productivity — aligned with real student needs in competitive academic environments.

### Future Improvements
- Add multilingual support (e.g., Hindi/regional languages).
- Save session history.
- Integrate more Groq models or offline options.

Solo project by Yuri
