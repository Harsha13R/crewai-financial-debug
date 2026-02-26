# ==============================
# task.py (Production Version)
# ==============================

from crewai import Task
from agents import (
    financial_analyst,
    investment_advisor,
    risk_assessor,
    verifier
)
from tools import read_financial_document


# ---------------------------------
# 1️⃣ Financial Analysis Task
# ---------------------------------
analyze_financial_document = Task(
    description="""
    Read the uploaded financial document using the provided tool.

    Perform a structured financial analysis including:
    1. Executive summary of the company's performance
    2. Key financial metrics (Revenue, Net Income, Operating Margin, EPS, Cash Flow)
    3. Year-over-year or quarterly performance trends (if available)
    4. Operational highlights

    Only use information explicitly available in the document.
    Do NOT fabricate data.
    """,

    expected_output="""
    A structured financial report containing:

    - Executive Summary
    - Key Financial Metrics
    - Performance Trends
    - Operational Insights
    """,

    agent=financial_analyst,
    tools=[read_financial_document],
    async_execution=False,
)


# ---------------------------------
# 2️⃣ Investment Insights Task
# ---------------------------------
investment_analysis = Task(
    description="""
    Based strictly on the analyzed financial data:

    1. Provide balanced investment insights.
    2. Highlight strengths and weaknesses.
    3. Discuss growth potential and financial stability.
    4. Avoid recommending specific financial products.
    5. Avoid exaggerated claims.

    Use professional, compliance-aware language.
    """,

    expected_output="""
    Structured investment insights including:

    - Strengths
    - Weaknesses
    - Growth Outlook
    - Balanced Investment Perspective
    """,

    agent=investment_advisor,
    async_execution=False,
)


# ---------------------------------
# 3️⃣ Risk Assessment Task
# ---------------------------------
risk_assessment = Task(
    description="""
    Identify financial and operational risks explicitly mentioned
    in the document.

    Categorize risks such as:
    - Market Risk
    - Operational Risk
    - Liquidity Risk
    - Regulatory Risk

    Do not exaggerate or fabricate risks.
    Only include risks supported by document evidence.
    """,

    expected_output="""
    A categorized risk analysis including:

    - Identified Risks
    - Risk Severity (Low / Medium / High)
    - Potential Impact
    - Risk Mitigation Discussion (if mentioned)
    """,

    agent=risk_assessor,
    async_execution=False,
)


# ---------------------------------
# 4️⃣ Document Verification Task
# ---------------------------------
verification = Task(
    description="""
    Verify that the uploaded file is a financial document.

    Confirm:
    - Presence of financial statements
    - Company name
    - Reporting period
    - Key financial terminology

    If document is not financial in nature, clearly state so.
    """,

    expected_output="""
    Verification report including:

    - Document Type Confirmation
    - Extracted Company Name
    - Reporting Period
    - Financial Content Validation
    """,

    agent=verifier,
    async_execution=False
)