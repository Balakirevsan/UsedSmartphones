from redis import Redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_redis_client() -> Redis:
    return Redis(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        password=os.getenv('REDIS_PASSWORD'),
        decode_responses=True
    )

redis_client = get_redis_client()