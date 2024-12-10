# Job_Application_Automation

## Overview
**Job_Application_Automation** is a Python-based application designed to assist job seekers in automating the job application process. This tool extracts key information from a job seeker's resume (e.g., personal details, work experience, skills, education) and automatically populates the relevant fields on job application forms across various platforms. This solution aims to save time and reduce the repetitive work involved in job applications.

With the power of modern AI, the application provides an intelligent, fast, and efficient way to streamline job application submissions.

---

## Features
- **Resume Parsing**: Automatically extracts critical information from resumes (PDF format).
- **Automatic Form Filling**: Based on the extracted data, the tool fills in fields on job application forms.
- **Streamlined User Interface**: Built with **Streamlit**, the user interface is simple, interactive, and easy to navigate.
- **Customizable**: The solution can be adapted to work with any application form with minimal effort.
- **AI Integration**: Uses **Google's Generative AI** for advanced data extraction and field predictions.
- **Multi-platform Compatibility**: Works across various job boards and application portals, helping job seekers on multiple platforms.

---

## Tech Stack
This project uses a combination of technologies to ensure efficient and intelligent job application automation:

### 🐍 **Python**  
The core programming language, providing robust tools for automation, PDF parsing, and backend logic.

### 🌐 **Streamlit**  
Streamlit was used to create the web interface, making the app highly interactive and easy to use with minimal setup.

### 🔒 **python-dotenv**  
Manages environment variables securely to store sensitive data like API keys, allowing smooth integration with external services without hardcoding credentials.

### 🤖 **Google Generative AI**  
Used for intelligent parsing and filling up application fields by analyzing and generating responses based on resume data.

### 📝 **PyPDF2**  
Helps extract text and data from PDF resumes, making it easier to automate the resume data extraction process.

### 🔎 **re (Regular Expressions)**  
Used for data extraction and cleaning from text, ensuring accurate field matching and improved accuracy in filling forms.

### 🎨 **CSS Styling in Streamlit**  
Streamlit’s ability to integrate custom CSS was utilized to style the application, giving it a professional and user-friendly interface.

---

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/Job_Application_Automation.git
    cd Job_Application_Automation
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables for secure API keys using a `.env` file. Make sure to configure it with the appropriate keys:
    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

---

## Usage

1. **Run the app** using Streamlit:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. **Upload your Resume**: Select the PDF resume you want to use for the application.

4. **Form Auto-Fill**: Once the resume is uploaded, the system will parse the resume using AI, extract relevant data, and fill out the respective fields in the job application form.

5. **Submit the Application**: After auto-filling the form, review the details, and submit it directly from the web interface.

---

## Example Workflow
1. **Upload Resume**: Job seeker uploads their resume in PDF format.
2. **AI Processing**: Google's Generative AI processes the resume and extracts data such as name, contact details, work experience, skills, and education.
3. **Automatic Field Filling**: The extracted data is used to automatically fill out application forms.
4. **Submit Applications**: The filled application form is ready for submission, saving the job seeker time and effort.

---

## Contributing

We welcome contributions to make **Job_Application_Automation** even better! To contribute, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes and open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Streamlit**: The amazing framework for creating web apps with Python.
- **Google Generative AI**: For advanced AI capabilities used in extracting and filling resume data.
- **PyPDF2**: For powerful PDF parsing and text extraction from resumes.
- **python-dotenv**: For secure management of environment variables.
- **CSS Styling**: Custom styling to enhance the look and feel of the Streamlit app.

---

## Contact

Feel free to reach out for any queries or collaboration opportunities:

- **GitHub**:[https://github.com/CodPritam](https://github.com/CodPritam)
- **Email**: p.pritam201@gmail.com
- **LinkedIn**:[https://linkedin.com/in/](https://www.linkedin.com/in/pritam-panigrahi-220731274/)
