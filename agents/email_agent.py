import re
from memory.memory_client import RedisMemoryClient
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
memory = RedisMemoryClient()

def extract_summary_and_urgency(content):
    prompt = f"""
You will receive an email. Your task is to:
1. Summarize it in 1–2 sentences.
2. Detect the urgency as "high", "medium", or "low".
3. Get Sender email address

Respond ONLY in this JSON format:
{{
  "summary": "...",
  "urgency": "...",
  "sender": "..."
}}

Email:
\"\"\"
{content}
\"\"\"
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        json_str = response.text.strip()
        
        json_str = json_str.strip("```json").strip("```").strip()
        print(f"LLM Response: {json_str}") 
        
        return json.loads(json_str)
    except Exception as e:
        # print(f"Error during LLM processing: {e}")
        return {
            "summary": "Summarization failed.",
            "urgency": "unknown",
            "sender": "unknown",
            "error": str(e)
        }

def process_email(content, thread_id):
    sender = re.search(r"From: (.+)", content)
    llm_result = extract_summary_and_urgency(content)

    result = {
        "sender": llm_result.get("sender", sender.group(1) if sender else "unknown"),
        "intent": llm_result.get("summary"),
        "urgency": llm_result.get("urgency")
    }
    memory.append_field(thread_id, "email_info", result)
    return {"status": "success", "data": result}
