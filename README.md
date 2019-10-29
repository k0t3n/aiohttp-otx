# AIOHTTP OTX

**AIOHTTP OTX** is aiohttp-based microservice that is used to obtain [OTX indicators](https://www.alienvault.com/documentation/usm-appliance/otx/about-otx.htm#About) over IPv4 addresses.

Responses are cached using Redis, see `app/views.py` for details.


## Requirements
 * Python >=3.7
 * Redis

## Installation
```bash
pip install -r requirements.txt
```

## Start
```bash
python main.py
```

Configs are located under `app/settings.py`