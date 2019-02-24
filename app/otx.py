import OTXv2
from OTXv2 import IndicatorTypes, OTXv2 as OTXv2Handler

from app.utils import add_updated_at_field


class OTXMachine:
    def __init__(self, api_key):
        self._connection = OTXv2Handler(api_key)

    def get_indicators_by_ip(self, ip):
        # TODO: multiple indicator types support
        try:
            data = add_updated_at_field(
                self._connection.get_indicator_details_full(
                    indicator_type=IndicatorTypes.IPv4,
                    indicator=ip
                )
            )

            return data
        except OTXv2.BadRequest:
            return None
