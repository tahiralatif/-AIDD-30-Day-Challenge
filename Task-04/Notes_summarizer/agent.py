from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import os
import asyncio
from dotenv import load_dotenv

# Import the tools from tools.py
from tools import (
    read_user_profile, update_user_profile, add_to_rag_memory, retrieve_from_rag_memory
)

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

# External Gemini Client
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta",
    timeout=120.0, # Increased timeout for potentially longer operations
)

# Model Configuration
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Runner configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# --- Main function to run the agent ---
async def main(task_type: str, content_text: str, quiz_type: str = "Multiple Choice", num_questions: int = 10, chat_query: str = None):
    """
    Runs the StudyNotesAgent to process content and returns the result based on task_type.
    """
    print(f"Agent main function called with task_type: {task_type}")

    base_instructions = (
        "You are an expert AI assistant for students. Your goal is to help users study more effectively. "
        "Your tone should be a mix of Roman Urdu and English, super desi, funny, and motivational. "
        "Always end your final output with: 'Now you'll become a topper, brother!'\n\n"
        "Here is the content you need to process:\n"
        f"{content_text}\n\n"
    )

    if task_type == "short_summary":
        instructions = base_instructions + (
            "Please provide a concise, easy-to-understand summary of the key points from the provided content, "
            "between 100-150 words. Focus on the most important information.\n\n"
            "Format your output as plain text."
        )
    elif task_type == "mindmap_summary":
        instructions = base_instructions + (
            "Please provide a mindmap-style bullet summary of the provided content. "
            "Use clear, hierarchical bullet points to break down concepts.\n\n"
            "Format your output using Markdown bullet points."
        )
    elif task_type == "detailed_summary":
        instructions = base_instructions + (
            "Please provide a detailed concept breakdown with examples from the provided content. "
            "Elaborate on the key ideas and illustrate them with relevant examples.\n\n"
            "Format your output using Markdown with clear headings and bullet points."
        )
    elif task_type == "student_doubts":
        instructions = base_instructions + (
            "Based on the provided content, identify the 5 most common student doubts and provide crystal clear answers for each. "
            "Ensure the answers are easy to understand for students.\n\n"
            "Format your output using Markdown with questions and answers clearly separated."
        )
    elif task_type == "generate_quiz":
        quiz_instruction_part = ""
        if quiz_type == "True/False":
            quiz_instruction_part = (
                f"Generate exactly {num_questions} 'True/False' questions based on the content. "
                "Each question must have a correct answer and a brief explanation.\n\n"
                "**Crucially, format your final output *exactly* as follows (JSON array of objects):**\n"
                "```json\n"
                "[\n"
                "  {\n"
                '    "question": "Is the sky blue?",\n'
                '    "options": ["True", "False"],\n'
                '    "answer": "True",\n'
                '    "explanation": "The sky is blue due to Rayleigh scattering."\n'
                "  },\n"
                "  // ... (9 more questions, with the 10th being a HILARIOUS Meme MCQ with nonsense distractors)\n"
                "]\n"
                "```"
            )
        else: # Multiple Choice
            quiz_instruction_part = (
                f"Generate exactly {num_questions} 'Multiple Choice' questions based on the content, with 4 options per question. "
                "Each question must have a correct answer and a brief explanation.\n\n"
                "**Crucially, format your final output *exactly* as follows (JSON array of objects):**\n"
                "```json\n"
                "[\n"
                "  {\n"
                '    "question": "What is the capital of France?",\n'
                '    "options": ["London", "Berlin", "Paris", "Madrid"],\n'
                '    "answer": "Paris",\n'
                '    "explanation": "Paris is the capital and most populous city of France."\n'
                "  },\n"
                "  // ... (9 more questions, with the 10th being a HILARIOUS Meme MCQ with nonsense distractors)\n"
                "]\n"
                "```"
            )
        instructions = base_instructions + quiz_instruction_part
        # Add specific instruction for meme MCQ for the agent to follow
        instructions += (
            f"\n\nRemember, the {num_questions}th question MUST be a HILARIOUS Meme MCQ with nonsense distractors. "
            "Make it super funny and desi!"
        )
    elif task_type == "chat":
        # Retrieve relevant context from RAG memory for the chat query
        relevant_context = retrieve_from_rag_memory(chat_query)
        instructions = base_instructions + (
            f"The user has asked a follow-up question: '{chat_query}'.\n"
            f"Here is some potentially relevant information from the document: '{relevant_context}'.\n"
            "Please answer the user's question concisely based on the provided content and the relevant information. "
            "If the information is not in the document, state that you cannot answer from the provided context.\n\n"
        )
    else:
        instructions = base_instructions + "Please provide a general response to the given content."

    # --- Define Agent with Dynamic Instructions ---
    study_agent = Agent(
        name="StudyBeast AI",
        instructions=instructions,
        model=model,
        tools=[read_user_profile, update_user_profile, add_to_rag_memory],
    )
    
    prompt = f"Process the content for a {task_type} task."
    print(f"Agent prompt: {prompt}")

    print("Calling Runner.run...")
    result = await Runner.run(study_agent, prompt, run_config=config)
    print("Runner.run completed.")

    if result and result.final_output:
        print("Agent returned a final output.")
        return result.final_output
    
    print("Agent did not return a final output or result was None.")
    return None

if __name__ == "__main__":
    print("Agent module run directly. This should typically be called from app.py.")
    # Example usage (for testing purposes, will remove later)
    # asyncio.run(main("short_summary", "The quick brown fox jumps over the lazy dog."))
