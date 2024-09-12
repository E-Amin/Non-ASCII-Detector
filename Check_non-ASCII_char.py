######################################################################################################
# This script is used to check for non-ASCII characters in a single text or FASTA file
# used in NGS genotyping pipelines.
# The script utilizes Streamlit to provide a web interface for the end-user
# To run the script, use the command: "python -m streamlit run Check_non-ASCII_char.py"
# This script was developed and tested by Eslam Ibrahim (Eslam.ibrahim@anu.edu.au) on August 12, 2024.
######################################################################################################
import streamlit as st
import pandas as pd
from Bio import SeqIO

# A function to check for non-ASCII characters in sequence headers
def check_non_ascii(file_content):
    results = []
    lines = file_content.splitlines()
    line_num = 1  # Start with the first line
    
    for line in lines:
        if line.startswith(">"):
            sequence_id = get_sequence_id(line)
            for idx, char in enumerate(line):
                if ord(char) > 127:  # ASCII characters have values from 0 to 127
                    results.append({
                        'Sequence ID': sequence_id,
                        'Non-ASCII Character': char,
                        'Position': idx + 1,
                        'Line Number': line_num,
                        'Header Line': line
                    })
        line_num += 1  # Move to the next line number
    return results

def get_sequence_id(header_line):
    sequence_id = header_line.lstrip('>')
    sequence_id = sequence_id.split()[0]
    return sequence_id

# Display text in title formatting.
st.title("FASTA/Text File Checker for Non-ASCII Characters")
st.write("Upload a FASTA or text file to check for non-ASCII characters in sequence headers.")

# uploading file fasta or txt format
uploaded_file = st.file_uploader("Choose a file", type=["fasta", "txt"])


if uploaded_file is not None:
    # decode("utf-8") used to convert from default format for file uploads to string using UTF-8 encoding
    file_content = uploaded_file.read().decode("utf-8")
    results = check_non_ascii(file_content)
    
    if results:
        st.write("The file contains non-ASCII characters in sequence headers.")
        df = pd.DataFrame(results)
        st.dataframe(df)
        #st.write(pd.DataFrame(results))
    else:
        st.write("The file passed: All sequence headers contain only ASCII characters.")

