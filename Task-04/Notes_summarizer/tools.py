import fitz # PyMuPDF
import pptx
import docx
import pandas as pd
from PIL import Image
# import easyocr
import yt_dlp
# import whisper # Commented out due to potential high dependency
import os

# Placeholder for a RAG system or memory
class AgentMemory:
    def __init__(self):
        self.chunks = [] # Store text chunks
        # In a real scenario, this would interact with a database like SQLite
    
    def add_chunk(self, text):
        self.chunks.append(text)
    
    def retrieve(self, query):
        # Simple retrieval for now, could be enhanced with embeddings
        relevant_chunks = [chunk for chunk in self.chunks if query.lower() in chunk.lower()]
        return " ".join(relevant_chunks)

agent_memory = AgentMemory()


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    text = ""
    try:
        doc = fitz.open(file_path)
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    return text

def extract_text_from_pptx(file_path: str) -> str:
    """
    Extracts text from a PPTX file. (Placeholder)
    """
    # Implementation using python-pptx
    return f"Text from PPTX: {file_path} (Not fully implemented yet)"

def extract_text_from_docx(file_path: str) -> str:
    """
    Extracts text from a DOCX file. (Placeholder)
    """
    # Implementation using python-docx
    return f"Text from DOCX: {file_path} (Not fully implemented yet)"

def extract_text_from_csv(file_path: str) -> str:
    """
    Extracts text from a CSV file. (Placeholder)
    """
    # Implementation using pandas
    return f"Text from CSV: {file_path} (Not fully implemented yet)"

def extract_text_from_txt(file_path: str) -> str:
    """
    Extracts text from a TXT file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return ""

# def extract_text_from_image(file_path: str) -> str:
#     """
#     Extracts text from an image file using EasyOCR. (Placeholder)
#     """
#     # Implementation using easyocr
#     # reader = easyocr.Reader(['en']) # You might need to download language models
#     # result = reader.readtext(file_path)
#     # text = " ".join([entry[1] for entry in result])
#     # return text

def get_youtube_transcript_and_summary(youtube_url: str) -> str:
    """
    Extracts transcript from YouTube URL using yt-dlp.
    Returns the raw transcript text. Summarization will be handled by the agent.
    """
    try:
        ydl_opts = {
            'writesubtitles': True,
            'subtitleslangs': ['en'],
            'skip_download': True,
            'format': 'bestaudio/best', # This is needed even with skip_download to correctly identify video
            'quiet': True,
            'no_warnings': True,
            'outtmpl': 'temp_transcript.vtt' # Output to a temporary VTT file
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            
            # Find the English transcript
            transcript_text = ""
            if 'requested_subtitles' in info and 'en' in info['requested_subtitles']:
                subtitle_url = info['requested_subtitles']['en']['url']
                import requests
                response = requests.get(subtitle_url)
                if response.status_code == 200:
                    # Basic parsing of VTT to extract text
                    lines = response.text.split('\n')
                    for line in lines:
                        if '-->' not in line and not line.startswith('WEBVTT') and line.strip() != '':
                            transcript_text += line.strip() + " "
            
            if transcript_text:
                return transcript_text.strip()
            else:
                return f"No English transcript found for the YouTube URL: {youtube_url}"

    except Exception as e:
        print(f"Error extracting YouTube transcript: {e}")
        return f"Error extracting YouTube transcript: {e}"

def read_user_profile():
    """
    Reads user profile information. (Placeholder)
    """
    return "User profile data (Not implemented)"

def update_user_profile(data):
    """
    Updates user profile information. (Placeholder)
    """
    return f"User profile updated with: {data} (Not implemented)"

# RAG related functions (simple in-memory for now)
def add_to_rag_memory(text: str):
    """
    Adds text to the RAG system's memory.
    """
    agent_memory.add_chunk(text)

def retrieve_from_rag_memory(query: str) -> str:
    """
    Retrieves relevant information from the RAG system's memory based on a query.
    """
    return agent_memory.retrieve(query)