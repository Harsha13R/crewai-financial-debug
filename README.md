# CrewAI Financial Document Analyser – Debugged Version

## Project Overview
This project is a financial document analyser system built using CrewAI.
The original codebase contained multiple bugs, which have been identified and fixed.

## Bugs Identified & Fixes

1. Import errors and incorrect module references
   - Fixed incorrect imports and dependency mismatches.

2. Agent configuration issues
   - Corrected agent roles and task definitions.

3. Tool execution errors
   - Fixed tool function parameters and return formats.

4. API call failures
   - Updated model initialization and environment variable handling.

## Setup Instructions

1. Clone the repository:
   git clone <your-repo-link>

2. Create virtual environment:
   python -m venv venv

3. Activate environment:
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the application:
   python main.py

## API Documentation

- Input: Financial PDF file
- Output: Structured financial analysis summary

## Improvements (Optional Bonus)

- Added error handling
- Improved logging
- Optimized agent workflow
