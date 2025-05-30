import json
from schemas.target_schema import TargetSchema
from memory.memory_client import RedisMemoryClient

memory = RedisMemoryClient()

def process_json(content, thread_id):
    try:
        # Handle both string and dictionary inputs
        if isinstance(content, str):
            data = json.loads(content)
        else:
            data = content
            
        print(f"Processing JSON data: {data}")
        
        # Validate required fields
        if not isinstance(data, dict):
            raise ValueError(f"Expected dictionary, got {type(data)}")
            
        if 'product' not in data:
            raise ValueError("Missing required field: 'product'")
        if 'quantity' not in data:
            raise ValueError("Missing required field: 'quantity'")
            
        validated = TargetSchema(**data)
        memory.append_field(thread_id, "extracted_fields", validated.dict())
        return {"status": "success", "data": validated.dict()}
    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON format: {str(e)}"
        print(error_msg)
        memory.append_field(thread_id, "error", error_msg)
        return {"status": "error", "message": error_msg}
    except Exception as e:
        error_msg = f"Error processing JSON: {str(e)}"
        print(error_msg)
        memory.append_field(thread_id, "error", error_msg)
        return {"status": "error", "message": error_msg}