import streamlit as st
import base64
from io import BytesIO


def main():
    st.title("Resume Upload App")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email Address")

    file = st.file_uploader("Upload your Resume", type=["pdf", "doc", "docx"])

    if st.button("Submit"):
        if file is not None and first_name and last_name and email:
            st.success("Resume Uploaded Successfully!")
            st.write("First Name:", first_name)
            st.write("Last Name:", last_name)
            st.write("Email Address:", email)

            # Convert the uploaded file to bytes
            file_bytes = file.getbuffer()

            # Create a download link for the file
            b64 = base64.b64encode(file_bytes).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/{file.type};base64,{b64}" download=\'{file.name}\'>\
            Click to download {file.name}</a>'

            st.markdown(href, unsafe_allow_html=True)

        else:
            st.error("Please fill all fields and upload a resume.")


if __name__ == "__main__":
    main()
