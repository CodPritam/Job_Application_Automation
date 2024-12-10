import streamlit as st
import json
import base64
from Parser import ResumeParser

# Function to set background
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set a dynamic background
set_background("D:\Projects pritam\Resume_parser_Gemini\Data\pexels-babybluecat-6847584.jpg")  # Ensure you have this image in your directory

# Initialize the ResumeParser
parser = ResumeParser()

# Streamlit App Title with animation effect
st.markdown(
    """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .animated-title {
        color: #FF0000;  /* Change title color */
        animation: blink 2s infinite;
        font-size: 2.5rem; /* Adjust size as needed */
        text-align: center;
    }
    .field-heading {
        color: #ffffff;  /* Change field heading color */
        font-size: 1.2rem;  /* Adjust size if needed */
        margin-bottom: 5px;
    }
    .field-label {
        color: #ffffff;  /* Change text input labels color */
    }
    </style>
    <h1 class="animated-title">Resume Autofill Job Application</h1>
    """,
    unsafe_allow_html=True
)

# Resume Upload Section
st.markdown('<p class="field-heading">Upload Your Resume</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    try:
        # Save the uploaded file temporarily
        with open("uploaded_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Parse the uploaded resume
        parsed_data = parser.parse_resume("uploaded_resume.pdf")
        cleaned_response = parsed_data.strip('```json\n```')

        # Parse the cleaned response
        try:
            json_data = json.loads(cleaned_response)
            st.sidebar.header("Parsed Resume Data")
            st.sidebar.json(json_data)

            # Job Application Form
            with st.form("job_application_form"):
                st.markdown(
                    """
                    <style>
                    .field-label {
                        color: white; /* Change label text color */
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown('<p class="field-heading">Job Application Form</p>', unsafe_allow_html=True)

                # Personal Details
                st.markdown('<p class="field-heading">Personal Details</p>', unsafe_allow_html=True)
                name = st.text_input("Full Name", json_data.get("Name", ""), label_visibility="visible")
                email = st.text_input("Email Address", json_data.get("Email", ""), label_visibility="visible")
                phone = st.text_input("Phone Number", json_data.get("Phone", ""), label_visibility="visible")
                address = st.text_area("Current Address", json_data.get("Address", ""), label_visibility="visible")

                # Additional Fields
                st.markdown('<p class="field-heading">Additional Details</p>', unsafe_allow_html=True)
                gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
                authorized = st.radio("Are you authorized to work in this country?", ["Yes", "No"])
                sponsorship = st.radio("Do you require sponsorship for employment?", ["Yes", "No"])
                position_applied = st.text_input("Position Applied For", "")
                preferred_location = st.text_input("Preferred Job Location", "")
                expected_salary = st.text_input("Expected Salary", "")
                start_date = st.date_input("Available Start Date")
                referral_source = st.text_input("Referral Source", "")
                date_of_birth = st.date_input("Date of Birth")
                permanent_address = st.text_area("Permanent Address", "")

                # Education Section
                st.markdown('<p class="field-heading">Education</p>', unsafe_allow_html=True)
                for edu in json_data.get("Education", []):
                    st.text_area(
                        f"Education: {edu['Institution']}",
                        f"{edu['Degree']} from {edu['Institution']}, {edu['Location']} "
                        f"(Completed: {edu['CompletionDate']}, Percentage: {edu['Percentage']})"
                    )

                # Experience Section
                st.markdown('<p class="field-heading">Experience</p>', unsafe_allow_html=True)
                for exp in json_data.get("Experience", []):
                    st.text_area(
                        f"Experience: {exp['Title']}",
                        f"{exp['Title']} at {exp['Company']} ({exp['Dates']})"
                    )

                # Skills Section
                st.markdown('<p class="field-heading">Skills</p>', unsafe_allow_html=True)
                st.text_area("Skills", ", ".join(json_data.get("Skills", [])))

                # Tools Section
                st.markdown('<p class="field-heading">Tools</p>', unsafe_allow_html=True)
                st.text_area("Tools", ", ".join(json_data.get("Tools", [])))

                # Additional Information
                st.markdown('<p class="field-heading">Additional Information</p>', unsafe_allow_html=True)
                about_you = st.text_area("Tell us about yourself", placeholder="Enter a short summary here...")

                # Form submission
                submitted = st.form_submit_button("Submit Application")
                if submitted:
                    st.success("Application Submitted Successfully!")
                    st.write("Here are the details you submitted:")
                    st.write(f"**Name:** {name}")
                    st.write(f"**Email:** {email}")
                    st.write(f"**Phone:** {phone}")
                    st.write(f"**Address:** {address}")
                    st.write(f"**Gender:** {gender}")
                    st.write(f"**Authorized to work:** {authorized}")
                    st.write(f"**Sponsorship required:** {sponsorship}")
                    st.write(f"**Position Applied For:** {position_applied}")
                    st.write(f"**Preferred Job Location:** {preferred_location}")
                    st.write(f"**Expected Salary:** {expected_salary}")
                    st.write(f"**Available Start Date:** {start_date}")
                    st.write(f"**Referral Source:** {referral_source}")
                    st.write(f"**Date of Birth:** {date_of_birth}")
                    st.write(f"**Permanent Address:** {permanent_address}")
                    st.write(f"**About You:** {about_you}")

                    # Celebratory Effect
                    st.balloons()  # Show balloons when the form is submitted

        except json.JSONDecodeError as e:
            st.error(f"Failed to parse response as JSON: {e}")

    except Exception as e:
        st.error(f"An error occurred while processing the resume: {e}")
else:
    st.info("Please upload a PDF resume to autofill the form.")
