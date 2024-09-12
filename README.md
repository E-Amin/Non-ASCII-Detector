# NonASCII-Detector

**NonASCII-Detector** is a Python tool with a Streamlit interface for identifying non-ASCII characters in text and FASTA files. It is designed to support NGS genotyping pipelines by ensuring that sequence headers conform to ASCII standards.

## Features

- Python-Based: Developed using Python for efficient processing.
- Streamlit Interface: Provides a user-friendly web interface for easy file uploads and analysis.
- Detailed Reports: Identifies non-ASCII characters in sequence headers, with reports including line numbers, character positions, and offending characters.

## Usage

1. Run the Script:
   python -m streamlit run Check_non-ASCII_char.py

2. Upload File:
   - Access the web interface at http://localhost:8501 after running the script.
   - Upload a FASTA or text file to check for non-ASCII characters in sequence headers.

3. View Results:
   - The script will display any non-ASCII characters found, along with details in a table format.

## Requirements

- Python: Ensure you have Python installed.
- Streamlit: Install Streamlit via pip:
  pip install streamlit
