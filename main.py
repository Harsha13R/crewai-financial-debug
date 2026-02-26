# ==============================
# main.py (Fixed & Production Safe)
# ==============================

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document as financial_task

app = FastAPI(title="Financial Document Analyzer")


# ---------------------------------
# Crew Runner (Synchronous)
# ---------------------------------
def run_crew(query: str, file_path: str):
    """Run CrewAI workflow with uploaded file"""

    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[financial_task],
        process=Process.sequential,
    )

    # Pass both query and file path
    result = financial_crew.kickoff({
        "query": query,
        "path": file_path
    })

    return result


# ---------------------------------
# Health Check
# ---------------------------------
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# ---------------------------------
# Analyze Endpoint
# ---------------------------------
@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        # Ensure directory exists
        os.makedirs("data", exist_ok=True)

        # Validate file type
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported."
            )

        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        if not query or query.strip() == "":
            query = "Analyze this financial document"

        # Run Crew in threadpool (prevents blocking event loop)
        response = await asyncio.to_thread(
            run_crew,
            query.strip(),
            file_path
        )

        return {
            "status": "success",
            "file_processed": file.filename,
            "analysis": str(response)
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing financial document: {str(e)}"
        )

    finally:
        # Cleanup file safely
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass


# ---------------------------------
# Local Run
# ---------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)