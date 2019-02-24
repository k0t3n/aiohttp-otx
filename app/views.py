import json

from aiohttp import web
from aiohttp.web_response import json_response

from app.otx import OTXMachine
from app.redis import RedisMachine
from app.utils import is_ip_valid

routes = web.RouteTableDef()


@routes.view('/api/v1/getIndicatorsByIP/')
class GetPulseByIPView(web.View):
    async def get(self):
        api_key = self.request.rel_url.query.get('api_key')
        ip = self.request.rel_url.query.get('ip')

        if api_key and is_ip_valid(ip):
            async with RedisMachine() as redis:
                key = f'{api_key}:{ip}'
                cached_value = await redis.get(key)
                if cached_value:
                    return json_response(json.loads(cached_value))

                data = OTXMachine(api_key).get_indicators_by_ip(ip)
                if data:
                    await redis.set(key, json.dumps(data))
                    return json_response(data)

                return json_response({'error': 'bad request to OTX'})

        return json_response({'error': 'api_token or ip params were not provided or invalid'}, status=400)
