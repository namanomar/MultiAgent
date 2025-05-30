import json
import mimetypes

def detect_format(content, filename=""):
    if filename.endswith(".pdf"):
        return "PDF"
    try:
        if isinstance(content, str):
            json.loads(content)
        elif isinstance(content, dict):
            pass  # Already a dictionary
        else:
            raise ValueError(f"Unexpected content type: {type(content)}")
        return "JSON"
    except Exception:
        return "Email"