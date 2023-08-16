import streamlit as st


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
        else:
            st.error("Please fill all fields and upload a resume.")


if __name__ == "__main__":
    main()
