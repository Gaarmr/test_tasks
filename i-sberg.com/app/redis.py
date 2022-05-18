import aioredis
from app.cfg import settings


redis = aioredis.from_url(settings.redis_url)