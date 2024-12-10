import PyPDF2  # For extracting text from PDF files
import google.generativeai as genai
import os
import json  # Import JSON for parsing response
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


class ResumeParser:
    def __init__(self):
        """
        Initializes the ResumeParser class with Google Generative AI model.
        """
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def extract_text_from_pdf(self, file_path):
        """
        Extracts text from a given PDF file.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Extracted text from the PDF.
        """
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            return ''.join([page.extract_text() for page in pdf_reader.pages])

    def parse_resume(self, file_path):
        """
        Parses resume details using Google Generative AI.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            dict: Parsed resume details in JSON format.
        """
        # Extract text from the resume PDF
        resume_text = self.extract_text_from_pdf(file_path)

        # Prompt for structured JSON output
        prompt = (
            f"Extract the following details from the resume in valid json string: "
            f"Name, Email, Phone, Address, Education (Institution, Location, Degree, CompletionDate, Percentage), "
            f"Experience (Title, Company, Dates), Skills, Tools:\n\n{resume_text}"
        )

        # Call the Generative AI model
        response = self.model.generate_content(f"{prompt}")

        # Debug: Print the raw response
        return response.text

        

# # Example usage (comment out when using in app.py)
# if __name__ == "__main__":
#     file_path = "D:/Projects pritam/Resume_parser_Gemini/Data/Pritam Panigrahi CVn.pdf"
#     parser = ResumeParser()
#     json_data=parser.parse_resume(file_path)
#     import json



# # Remove the ```json and ``` from the raw response
# cleaned_response = json_data.strip('```json\n```')

# # Parse the cleaned response
# try:
#     json_data = json.loads(cleaned_response)
#     print("Valid JSON")
#     print(json.dumps(json_data, indent=4))
# except json.JSONDecodeError as e:
#     print("Failed to parse response as JSON:", e)


    
