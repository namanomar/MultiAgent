import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def classify_intent(content):
    prompt = f"""Classify the intent of this text:
{content}
Intent (Invoice, RFQ, Complaint, Regulation):"""
    
    response = model.generate_content(prompt)
    return response.text.strip()

