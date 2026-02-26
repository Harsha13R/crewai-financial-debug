# ==============================
# agents.py (Production Version)
# ==============================

import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import read_financial_document

# ------------------------------
# Initialize LLM properly
# ------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,  # Low temperature for factual analysis
)

# ------------------------------
# Financial Analyst Agent
# ------------------------------

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Analyze the uploaded financial document and extract factual financial insights "
        "based strictly on the document content."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly experienced financial analyst specializing in corporate "
        "financial statements, earnings reports, and investment analysis. "
        "You rely strictly on verifiable data from the provided document. "
        "You do not speculate, hallucinate, or fabricate financial advice."
    ),
    tools=[read_financial_document],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

# ------------------------------
# Document Verifier Agent
# ------------------------------

verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Verify that the uploaded file is a valid financial document and ensure "
        "that extracted information matches the document content."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a compliance-focused financial document reviewer. "
        "Your job is to validate authenticity, detect inconsistencies, "
        "and ensure that all financial insights are grounded in the source document."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ------------------------------
# Investment Insight Agent
# ------------------------------

investment_advisor = Agent(
    role="Investment Research Analyst",
    goal=(
        "Provide balanced, document-based investment insights derived from "
        "the financial data presented in the report."
    ),
    verbose=True,
    backstory=(
        "You are a professional investment research analyst. "
        "You provide risk-aware, data-backed insights. "
        "You do not promote specific financial products. "
        "You avoid exaggerated claims and ensure regulatory-safe language."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# ------------------------------
# Risk Assessment Agent
# ------------------------------

risk_assessor = Agent(
    role="Financial Risk Analyst",
    goal=(
        "Identify and assess financial risks explicitly mentioned in the document, "
        "including operational, market, credit, or liquidity risks."
    ),
    verbose=True,
    backstory=(
        "You are a professional risk management specialist with experience "
        "in corporate financial risk analysis. "
        "You evaluate risk factors conservatively and based only on documented evidence."
    ),
    llm=llm,
    max_iter=2,
    allow_delegation=False
)