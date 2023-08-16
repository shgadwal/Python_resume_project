import os
import streamlit as st
from docx import Document
import PyPDF4
from datetime import datetime

MAX_FILE_SIZE = 1000000  # Maximum file size in bytes


def convert_docx_to_text(file):
    """Converts a .docx file to text."""
    document = Document(file)
    return " ".join([paragraph.text for paragraph in document.paragraphs])


def convert_pdf_to_text(file):
    """Converts a .pdf file to text."""
    pdf = PyPDF4.PdfFileReader(file)
    return " ".join([page.extractText() for page in pdf.pages])


def save_text_to_file(text, filename):
    """Saves the given text to a file."""
    with open(filename, "w") as f:
        f.write(text)


def generate_save_path(first_name, last_name):
    """Generates a save path for the text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{first_name}_{last_name}_{timestamp}.txt"
    return os.path.join("saved_files", filename)


def validate_file_size(file):
    """Validates the file size."""
    if file.size > MAX_FILE_SIZE:
        return False
    return True


def main():
    st.title("Resume Upload App")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email Address")

    file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])

    if st.button("Submit"):
        if file is not None and first_name and last_name and email:
            if not validate_file_size(file):
                st.error(f"File size should be less than {MAX_FILE_SIZE / 1000000} MB")
                return
            if file.type == "application/pdf":
                text = convert_pdf_to_text(file)
            elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = convert_docx_to_text(file)
            else:
                st.error("Unsupported file type")
                return
            save_path = generate_save_path(first_name, last_name)
            save_text_to_file(text, save_path)
            st.success("Resume Uploaded Successfully!")
            st.write("First Name:", first_name)
            st.write("Last Name:", last_name)
            st.write("Email Address:", email)
        else:
            st.error("Please fill all fields and upload a resume.")


if __name__ == "__main__":
    main()
