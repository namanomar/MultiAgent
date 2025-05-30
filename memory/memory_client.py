import redis
import json
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

class RedisMemoryClient:
    def __init__(self, host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"), db=0, password=os.environ.get("REDIS_PASSWORD"), url=None, ssl=False):
        
        self.client = redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                decode_responses=True,
                username="default",
                ssl=ssl
            )

    def set(self, thread_id, data):
        data['timestamp'] = datetime.utcnow().isoformat()
        self.client.set(thread_id, json.dumps(data))

    def get(self, thread_id):
        value = self.client.get(thread_id)
        return json.loads(value) if value else None

    def append_field(self, thread_id, key, value):
        data = self.get(thread_id) or {}
        data[key] = value
        self.set(thread_id, data)

    def delete(self, thread_id):
        self.client.delete(thread_id)
