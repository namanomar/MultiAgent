from datetime import datetime
from functions.format_detector import detect_format
from functions.intent_classifier import classify_intent
from memory.memory_client import RedisMemoryClient
from agents.json_agent import process_json
from agents.email_agent import process_email

memory = RedisMemoryClient()

def classify_and_route(content, filename=""):
    format_type = detect_format(content, filename)
    # print(format_type)
    intent = classify_intent(content)

    thread_id = f"{format_type.lower()}:{intent.lower()}:{datetime.utcnow().isoformat()}"
    memory.set(thread_id, {"format": format_type, "intent": intent})

    if format_type == "JSON":
        process_json(content, thread_id)
    elif format_type == "Email":
        process_email(content, thread_id)
    else:
        print(f"Unsupported format: {format_type}")
