import ipaddress
from datetime import datetime


def is_ip_valid(ip):
    """
    Returns True is IP is valid
    Supports IPv4 and IPv6
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def add_updated_at_field(data: dict) -> dict:
    """
    Adds `updated_at` field to dict
    """
    data['updated_at'] = str(datetime.now())

    return data
