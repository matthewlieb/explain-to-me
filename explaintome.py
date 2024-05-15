import os
import threading
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model using the API key from the environment variable
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set the page configuration as the first command in the script
st.set_page_config(page_title="ExplainToMe.ai", layout="wide")

def get_explanation(skill_level, topic):
    if not topic:
        return "Please enter a topic."
    prompt = f"Explain to someone at the {skill_level} level: {topic}"
    with st.spinner(f'Loading explanation for {skill_level} level...'):
        response = llm.invoke(prompt)
        return response.content if response else "Failed to fetch explanation."

def generate_trivia_questions(skill_level, topic, num_questions=3):
    if not topic:
        return ["Please enter a topic."] * num_questions
    difficulty = {
        'Novice': 'very simple',
        'Intermediate': 'moderate',
        'Advanced': 'complex',
        'Expert': 'very complex'
    }
    prompt = f"Create {num_questions} {difficulty[skill_level]} multiple choice trivia questions about {topic}, each with four options and indicate the correct answer, followed by an explanation."
    with st.spinner(f'Generating {skill_level} level trivia questions...'):
        response = llm.invoke(prompt)
        questions = response.content.split('\n\n') if response else []
        filtered_questions = [q for q in questions if len(q.strip().split('\n')) >= 6]
        while len(filtered_questions) < 3:
            filtered_questions.append("Not enough data for a complete question.\n" * 6)
        return filtered_questions[:3]

# Function to search and store results in session state
def search_topic(skill_level, topic):
    explanation_key = f'explanation_{skill_level}'
    question_key = f'questions_{skill_level}'
    st.session_state[explanation_key] = get_explanation(skill_level, topic)
    st.session_state[question_key] = generate_trivia_questions(skill_level, topic)

# Background search function
def search_all_levels(topic):
    for level in skill_levels:
        search_topic(level, topic)

st.title('ExplainToMe.ai')

# Sidebar for topic input and search button
with st.sidebar:
    with st.form(key='search_form'):
        topic_input = st.text_input("Enter a topic to explain:", key='universal_topic_input')
        search_button = st.form_submit_button(label='Search')

# Skill levels and corresponding tabs
skill_levels = ["Novice", "Intermediate", "Advanced", "Expert"]
tabs = st.tabs(skill_levels)

# Trigger search on form submission
if search_button and topic_input:
    st.session_state['current_skill_level'] = skill_levels[0]  # Set the initial current skill level
    search_topic(st.session_state['current_skill_level'], topic_input)
    
    # Start background threads for other skill levels
    for level in skill_levels:
        if level != st.session_state['current_skill_level']:
            threading.Thread(target=search_topic, args=(level, topic_input)).start()

for i, skill_level in enumerate(skill_levels):
    tab = tabs[i]
    with tab:
        explanation_key = f'explanation_{skill_level}'
        question_key = f'questions_{skill_level}'

        # Set the current skill level based on the tab the user clicks
        if st.session_state.get('current_skill_level') != skill_level:
            st.session_state['current_skill_level'] = skill_level
            if topic_input and explanation_key not in st.session_state:
                search_topic(skill_level, topic_input)

        # Display explanation if available
        if explanation_key in st.session_state:
            st.text_area("Explanation:", value=st.session_state.get(explanation_key, ""), height=150, key=f'text_area_{explanation_key}')

        # Display trivia questions if available
        if question_key in st.session_state:
            cols = st.columns(3)
            for j, full_question in enumerate(st.session_state.get(question_key, [])[:3]):
                with cols[j]:
                    question_parts = full_question.strip().split('\n')
                    if len(question_parts) >= 6:
                        question = question_parts[0]
                        answers = question_parts[1:5]
                        correct_answer = question_parts[5].split(':', 1)[1].strip() if ':' in question_parts[5] else "Correct answer not found"
                        explanation = question_parts[6].split(':', 1)[1].strip() if len(question_parts) > 6 and ':' in question_parts[6] else "No explanation provided."
                        st.subheader(question)
                        selected_answer = st.radio("Choose an answer:", answers, key=f'option_{skill_level}_{i}_{j}')
                        show_answer = st.button("Show Correct Answer", key=f'answer_{skill_level}_{i}_{j}', use_container_width=True)
                        if show_answer:
                            st.success(f"Correct Answer: {correct_answer}")
                            st.info(f"Explanation: {explanation}")
                    else:
                        st.error("Insufficient data to display this question properly.")

# Apply CSS styling
st.markdown("""
<style>
    .css-18e3th9 {
        background-color: #f0f2f6;
        border-radius: 10px;
        border: 2px solid #79aec8;
    }
    .stButton>button {
        color: white;
        background-color: #0d6efd;
        border-radius: 10px;  /* Reduced the border radius to make buttons smaller */
        border: none;
        padding: 4px 12px;  /* Reduced padding to make buttons smaller */
        font-size: 12px;  /* Reduced font size to make buttons smaller */
        font-weight: bold;
    }
    .stTextInput>div>div>input, .stRadio>label {
        border-radius: 20px;
        padding: 10px;
    }
    .st-bx {
        color: #4a4a4a;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)