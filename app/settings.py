from aiohttp_jwt import JWTMiddleware

JWT_SECRET_KEY = 'secret'

REDIS_URL = 'redis://localhost'
REDIS_KEY_EXPIRE_SECONDS = 86400

MIDDLEWARES = [
    JWTMiddleware(
        secret_or_pub_key=JWT_SECRET_KEY,
        auth_scheme='JWT',
    )
]
