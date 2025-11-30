import streamlit as st
import os
import sys
import asyncio
import tempfile
from pathlib import Path

# Ensure the StudyBeast directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Import agent and tools (will uncomment as they become fully functional)
from agent import main as run_agent
from tools import (
    extract_text_from_pdf, extract_text_from_pptx, extract_text_from_docx,
    extract_text_from_csv, get_youtube_transcript_and_summary,
    extract_text_from_txt, add_to_rag_memory, retrieve_from_rag_memory
)

# --- Page Configuration ---
st.set_page_config(
    page_title="StudyBeast",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for a more polished, shadcn-inspired look ---
st.markdown("""
<style>
    /* --- Root Variables for Colors and Fonts --- */
    :root {
        --primary-color: #6a11cb; /* A deep, vibrant purple */
        --secondary-color: #2575fc; /* A bright, energetic blue */
        --background-color: #f0f2f6; /* A very light, neutral gray */
        --sidebar-background-color: #ffffff;
        --card-background-color: #ffffff;
        --text-color: #1a1a2e; /* A dark, almost-black for high contrast */
        --subtle-text-color: #5a5a6e;
        --border-color: #e0e0e0;
        --border-radius: 0.75rem;
        --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.04);
        --font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* --- General Body and Container Styling --- */
    body {
        font-family: var(--font-family);
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .main .block-container {
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    /* --- Header and Title Styling --- */
    h1, h2, h3 {
        font-weight: 600;
        color: var(--text-color);
    }
    .st-emotion-cache-10trblm { /* Main title element */
        font-size: 2.5em;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    st.markdown:first-of-type > .stMarkdown { /* Subtitle under the main title */
        text-align: center;
        color: var(--subtle-text-color);
        font-size: 1.1em;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    /* --- Sidebar Styling --- */
    .st-emotion-cache-16txtl3 { /* Sidebar main container */
        background-color: var(--sidebar-background-color);
        border-right: 1px solid var(--border-color);
    }
    .st-emotion-cache-16txtl3 .st-emotion-cache-1d0Tzns { /* Expander header */
        font-weight: 500;
    }
    .st-emotion-cache-16txtl3 .stMarkdown { /* Sidebar footer text */
        color: var(--subtle-text-color);
        font-size: 0.9em;
    }

    /* --- Tab Styling --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        border-bottom: 1px solid var(--border-color);
    }
    .stTabs [data-baseweb="tab-list"] button {
        background-color: transparent;
        border-radius: var(--border-radius) var(--border-radius) 0 0;
        padding: 0.75rem 1.5rem;
        border: none;
        color: var(--subtle-text-color);
        border-bottom: 2px solid transparent;
        transition: color 0.2s, border-color 0.2s;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: var(--primary-color);
        border-bottom: 2px solid var(--primary-color);
    }
    .stTabs [data-baseweb="tab-list"] button:hover {
        background-color: rgba(0, 0, 0, 0.02);
        color: var(--primary-color);
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding: 1.5rem 0;
    }

    /* --- Card-like containers for input sections --- */
    .st-emotion-cache-1r4qj8v { /* Main container for sections like Paste Text, Upload Files */
        background-color: var(--card-background-color);
        border-radius: var(--border-radius);
        padding: 1.5rem 2rem;
        box-shadow: var(--box-shadow);
        border: 1px solid var(--border-color);
        margin-bottom: 1.5rem;
    }
    .st-emotion-cache-1r4qj8v h3 {
        margin-top: 0;
    }

    /* --- Button Styling --- */
    .stButton>button {
        background-image: linear-gradient(45deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        border-radius: var(--border-radius);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: none;
        transition: transform 0.2s, box-shadow 0.2s;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 10px rgba(106, 17, 203, 0.2);
        color: white;
    }
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* --- Input & Text Area Styling --- */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
        padding: 0.75rem 1rem;
        background-color: var(--background-color);
        color: var(--text-color);
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 2px rgba(106, 17, 203, 0.2);
    }

    /* --- File Uploader Styling --- */
    .stFileUploader > div > button {
        border-radius: var(--border-radius);
        border: 1px dashed var(--primary-color);
        background-color: rgba(106, 17, 203, 0.05);
        color: var(--primary-color);
        padding: 1rem;
    }
    .stFileUploader > div > button:hover {
        background-color: rgba(106, 17, 203, 0.1);
        color: var(--primary-color);
    }

    /* --- Alert/Message Styling --- */
    .stAlert {
        border-radius: var(--border-radius);
        border: 1px solid transparent;
    }
    .stAlert[data-testid="stAlert-info"] {
        background-color: rgba(37, 117, 252, 0.1);
        border-color: var(--secondary-color);
        color: #1a1a2e;
    }
    .stAlert[data-testid="stAlert-success"] {
        background-color: rgba(0, 192, 115, 0.1);
        border-color: #00c073;
    }
    .stAlert[data-testid="stAlert-warning"] {
        background-color: rgba(255, 179, 0, 0.1);
        border-color: #ffb300;
    }
    .stAlert[data-testid="stAlert-error"] {
        background-color: rgba(255, 48, 48, 0.1);
        border-color: #ff3030;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>StudyBeast 🧠📚</h1>", unsafe_allow_html=True)
st.markdown("Your ultimate AI study companion! Paste, upload, or link to get summaries, quizzes, and answers.")

# --- Sidebar ---
with st.sidebar:
    st.header("Session History")
    
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if st.session_state.history:
        for i, session in enumerate(st.session_state.history):
            with st.expander(f"{session['title']}"):
                st.write(f"Type: {session['content_type']}")
                if st.button(f"Load this session", key=f"load_session_{i}"):
                    st.session_state.processed_content = {"type": session['content_type'], "content": session['content']}
                    st.session_state.current_content_title = session['title']
                    st.session_state.messages = session.get('messages', []) # Ensure messages exists
                    st.rerun()
    else:
        st.info("No study sessions yet. Start learning!")
    
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: var(--subtle-text-color); font-size: 0.9em;'>Made with Gemini 1.5 Flash • Free Forever</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: var(--subtle-text-color); font-size: 0.9em;'>StudyBeast 2025</div>", unsafe_allow_html=True)


# --- Main Content Tabs ---
tab_titles = ["📤 Upload", "📝 Summary", "❓ Quiz", "💬 Chat (RAG)"]
tabs = st.tabs(tab_titles)

with tabs[0]: # Upload Tab
    st.header("Get Started in Seconds 🚀")
    st.write("Provide your study material through one of the methods below. StudyBeast will handle the rest.")
    
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            st.subheader("📝 Paste Text")
            pasted_text = st.text_area("Paste your content here...", height=150, key="pasted_text_input", label_visibility="collapsed")
            if st.button("Process Text", key="process_text_btn"):
                if pasted_text:
                    with st.spinner("Analyzing..."):
                        add_to_rag_memory(pasted_text)
                        st.session_state.processed_content = {"type": "text", "content": pasted_text}
                        st.session_state.current_content_title = "Pasted Text"
                        st.session_state.history.insert(0, {"title": "Pasted Text", "content_type": "text", "content": pasted_text, "messages": []})
                        st.session_state.history = st.session_state.history[:10]
                    st.success("Text ready!")
                else:
                    st.warning("Text box is empty!")

    with col2:
        with st.container():
            st.subheader("📄 Upload File")
            uploaded_file = st.file_uploader(
                "PDF, PPTX, DOCX, CSV, TXT",
                type=["pdf", "pptx", "docx", "csv", "txt"],
                key="file_uploader_input",
                label_visibility="collapsed"
            )
            if uploaded_file:
                with st.spinner(f"Processing {uploaded_file.name}..."):
                    file_extension = Path(uploaded_file.name).suffix.lower()
                    content_type = ""
                    try:
                        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_file_path = tmp_file.name

                        if file_extension == ".pdf":
                            extracted_content = extract_text_from_pdf(tmp_file_path)
                            content_type = "PDF"
                        elif file_extension == ".pptx":
                            extracted_content = extract_text_from_pptx(tmp_file_path)
                            content_type = "PPTX"
                        elif file_extension == ".docx":
                            extracted_content = extract_text_from_docx(tmp_file_path)
                            content_type = "DOCX"
                        elif file_extension == ".csv":
                            extracted_content = extract_text_from_csv(tmp_file_path)
                            content_type = "CSV"
                        elif file_extension == ".txt":
                            extracted_content = extract_text_from_txt(tmp_file_path)
                            content_type = "TXT"
                        
                        os.unlink(tmp_file_path)

                        if extracted_content:
                            add_to_rag_memory(extracted_content)
                            st.session_state.processed_content = {"type": content_type, "content": extracted_content}
                            st.session_state.current_content_title = f"{uploaded_file.name} ({content_type})"
                            st.session_state.history.insert(0, {"title": st.session_state.current_content_title, "content_type": content_type, "content": extracted_content, "messages": []})
                            st.session_state.history = st.session_state.history[:10]
                            st.success(f"{uploaded_file.name} ready!")
                        else:
                            st.error(f"Could not extract text from '{uploaded_file.name}'.")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                        if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                            os.unlink(tmp_file_path)

    with col3:
        with st.container():
            st.subheader("🔗 YouTube URL")
            youtube_url = st.text_input("Enter YouTube URL here...", key="youtube_url_input", label_visibility="collapsed")
            if st.button("Process URL", key="process_url_btn"):
                if youtube_url:
                    with st.spinner("Fetching transcript..."):
                        transcript = get_youtube_transcript_and_summary(youtube_url)
                        if transcript and not transcript.startswith("Error"):
                            add_to_rag_memory(transcript)
                            st.session_state.processed_content = {"type": "YouTube", "content": transcript}
                            st.session_state.current_content_title = f"YouTube: {youtube_url.split('v=')[-1]}"
                            st.session_state.history.insert(0, {"title": st.session_state.current_content_title, "content_type": "YouTube", "content": transcript, "messages": []})
                            st.session_state.history = st.session_state.history[:10]
                            st.success("Transcript ready!")
                        else:
                            st.error(f"Failed to get transcript. {transcript}")
                else:
                    st.warning("URL box is empty!")


def get_current_processed_content():
    return st.session_state.get("processed_content", {}).get("content", "")

async def run_agent_async(task_type: str, content: str, quiz_type: str = "Multiple Choice", num_questions: int = 10, chat_query: str = None):
    if task_type == "generate_quiz":
        return await run_agent(task_type, content, quiz_type, num_questions)
    elif task_type == "chat":
        return await run_agent(task_type, content, chat_query=chat_query)
    else:
        return await run_agent(task_type, content)

with tabs[1]: # Summary Tab
    st.header("Generate Insights from Your Content")
    if "processed_content" in st.session_state and st.session_state.processed_content.get("content"):
        st.info(f"Content from '{st.session_state.current_content_title}' is ready. Choose a summary type below.")
        
        summary_display_area = st.container()

        # Use columns for a cleaner button layout
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Generate Short Summary"):
                content = get_current_processed_content()
                if content:
                    with summary_display_area.spinner("Generating short summary..."):
                        try:
                            result = asyncio.run(run_agent_async("short_summary", content))
                            if result:
                                summary_display_area.success("Short summary generated successfully!")
                                summary_display_area.markdown(result)
                            else:
                                summary_display_area.error("Failed to generate short summary.")
                        except Exception as e:
                            summary_display_area.error(f"An error occurred: {e}")
                else:
                    summary_display_area.error("No content processed yet.")

            if st.button("Generate Mindmap-style Bullet Summary"):
                content = get_current_processed_content()
                if content:
                    with summary_display_area.spinner("Generating mindmap summary..."):
                        try:
                            result = asyncio.run(run_agent_async("mindmap_summary", content))
                            if result:
                                summary_display_area.success("Mindmap summary generated successfully!")
                                summary_display_area.markdown(result)
                            else:
                                summary_display_area.error("Failed to generate mindmap summary.")
                        except Exception as e:
                            summary_display_area.error(f"An error occurred: {e}")
                else:
                    summary_display_area.error("No content processed yet.")
        with col2:
            if st.button("Generate Detailed Concept Breakdown"):
                content = get_current_processed_content()
                if content:
                    with summary_display_area.spinner("Generating detailed summary..."):
                        try:
                            result = asyncio.run(run_agent_async("detailed_summary", content))
                            if result:
                                summary_display_area.success("Detailed summary generated successfully!")
                                summary_display_area.markdown(result)
                            else:
                                summary_display_area.error("Failed to generate detailed summary.")
                        except Exception as e:
                            summary_display_area.error(f"An error occurred: {e}")
                else:
                    summary_display_area.error("No content processed yet.")
            if st.button("Identify 5 Common Student Doubts"):
                content = get_current_processed_content()
                if content:
                    with summary_display_area.spinner("Generating student doubts..."):
                        try:
                            result = asyncio.run(run_agent_async("student_doubts", content))
                            if result:
                                summary_display_area.success("Student doubts generated successfully!")
                                summary_display_area.markdown(result)
                            else:
                                summary_display_area.error("Failed to generate student doubts.")
                        except Exception as e:
                            summary_display_area.error(f"An error occurred: {e}")
                else:
                    summary_display_area.error("No content processed yet.")
    else:
        st.warning("Please upload or paste content in the '📤 Upload' tab first to get started.")

with tabs[2]: # Quiz Tab
    st.header("Test Your Knowledge")
    if "processed_content" in st.session_state and st.session_state.processed_content.get("content"):
        st.info(f"Ready to generate a quiz from '{st.session_state.current_content_title}'.")
        quiz_type = st.radio("Choose Quiz Type:", ("Multiple Choice", "True/False"), key="quiz_type_radio", horizontal=True)
        quiz_display_area = st.container()
        if st.button("Brother, Generate 10 MCQs for Me"):
            content = get_current_processed_content()
            if content:
                with quiz_display_area.spinner(f"Generating {quiz_type} quiz..."):
                    try:
                        result = asyncio.run(run_agent_async("generate_quiz", content, quiz_type=quiz_type, num_questions=10))
                        if result:
                            quiz_display_area.success("Quiz generated successfully!")
                            quiz_display_area.markdown(result)
                        else:
                            quiz_display_area.error("Failed to generate quiz.")
                    except Exception as e:
                        quiz_display_area.error(f"An error occurred: {e}")
            else:
                quiz_display_area.error("No content processed yet.")
    else:
        st.warning("Please upload or paste content in the '📤 Upload' tab first to create a quiz.")

with tabs[3]: # Chat (RAG) Tab
    st.header("Chat with Your Document")
    if "processed_content" in st.session_state and st.session_state.processed_content.get("content"):
        st.info(f"You can now ask questions about the content from '{st.session_state.current_content_title}'.")

        # Initialize or retrieve chat history from session state
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input field
        if chat_query := st.chat_input("Ask a follow-up question..."):
            # Add user message to history and display it
            st.session_state.messages.append({"role": "user", "content": chat_query})
            with st.chat_message("user"):
                st.markdown(chat_query)

            # Generate and display assistant response
            with st.chat_message("assistant"):
                chat_display_area = st.empty()
                content = get_current_processed_content()
                if content:
                    with chat_display_area.spinner("Thinking..."):
                        try:
                            agent_response = asyncio.run(run_agent_async("chat", content, chat_query=chat_query))
                            if agent_response:
                                chat_display_area.markdown(agent_response)
                                st.session_state.messages.append({"role": "assistant", "content": agent_response})
                            else:
                                agent_response = "I'm sorry, but I encountered an error. Please try asking in a different way."
                                chat_display_area.markdown(agent_response)
                                st.session_state.messages.append({"role": "assistant", "content": agent_response})
                        except Exception as e:
                            agent_response = f"An error occurred: {e}"
                            chat_display_area.error(agent_response)
                            st.session_state.messages.append({"role": "assistant", "content": agent_response})
                else:
                    agent_response = "No content processed to chat with."
                    chat_display_area.warning(agent_response)
                    st.session_state.messages.append({"role": "assistant", "content": agent_response})

    else:
        st.warning("Please upload or paste content in the '📤 Upload' tab to start a chat session.")

# The main_loop and if __name__ == "__main__": block is no longer needed
# as asyncio.run is called directly within the button actions.

