from flask_redis import FlaskRedis
import os

class ContentManager():
    def __init__(self, app):
        redis_host = os.environ.get("REDIS_HOST", default="127.0.0.1")
        redis_port = os.environ.get("REDIS_PORT", default="6379")
        app.config['REDIS_URL'] = f"redis://{redis_host}:{redis_port}"
        self.redis_client = FlaskRedis(app)

    def get_content(self, contentKey):
        return self.redis_client.get(contentKey)

    def set_content(self, contentKey, contentValue):
        return self.redis_client.set(contentKey, contentValue)
