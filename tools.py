# ==============================
# tools.py (Production Version)
# ==============================

import os
from dotenv import load_dotenv
load_dotenv()

from pypdf import PdfReader
from langchain.tools import tool

# Optional: Search tool (only if SERPER_API_KEY exists)
try:
    from crewai_tools.tools.serper_dev_tool import SerperDevTool
    search_tool = SerperDevTool()
except Exception:
    search_tool = None


# ---------------------------------
# Financial Document PDF Reader Tool
# ---------------------------------

@tool
def read_financial_document(path: str) -> str:
    """
    Reads text from a PDF file.
    
    Args:
        path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from PDF
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found at path: {path}")

    try:
        reader = PdfReader(path)
    except Exception as e:
        raise ValueError(f"Error reading PDF file: {str(e)}")

    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text = text.strip()
            while "\n\n" in text:
                text = text.replace("\n\n", "\n")
            full_text += text + "\n"

    if not full_text.strip():
        raise ValueError("PDF appears empty or unreadable.")

    return full_text.strip()