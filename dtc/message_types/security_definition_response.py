
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class SecurityDefinitionResponse(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 symbol=None,
                 exchange=None,
                 security_type=None,
                 description=None,
                 min_price_increment=None,
                 price_display_format=None,
                 currency_value_per_increment=None,
                 is_final_message=None,
                 float_to_int_price_multiplier=None,
                 int_to_float_price_divisor=None,
                 underlying_symbol=None,
                 updates_bid_ask_only=None,
                 strike_price=None,
                 put_or_call=None,
                 short_interest=None,
                 security_expiration_date=None,
                 buy_rollover_interest=None,
                 sell_rollover_interest=None,
                 earnings_per_share=None,
                 shares_outstanding=None,
                 int_to_float_quantity_divisor=None,
                 has_market_depth_data=None,
                 display_price_multiplier=None,
                 exchange_symbol=None,
                 initial_margin_requirement=None,
                 maintenance_margin_requirement=None,
                 currency=None,
                 contract_size=None,
                 open_interest=None):
        self.Type = MessageTypes.SECURITY_DEFINITION_RESPONSE
        self.RequestID = request_id
        self.Symbol = symbol
        self.Exchange = exchange
        self.SecurityType = security_type
        self.Description = description
        self.MinPriceIncrement = min_price_increment
        self.PriceDisplayFormat = price_display_format
        self.CurrencyValuePerIncrement = currency_value_per_increment
        self.IsFinalMessage = is_final_message
        self.FloatToIntPriceMultiplier = float_to_int_price_multiplier
        self.IntToFloatPriceDivisor = int_to_float_price_divisor
        self.UnderlyingSymbol = underlying_symbol
        self.UpdatesBidAskOnly = updates_bid_ask_only
        self.StrikePrice = strike_price
        self.PutOrCall = put_or_call
        self.ShortInterest = short_interest
        self.SecurityExpirationDate = security_expiration_date
        self.BuyRolloverInterest = buy_rollover_interest
        self.SellRolloverInterest = sell_rollover_interest
        self.EarningsPerShare = earnings_per_share
        self.SharesOutstanding = shares_outstanding
        self.IntToFloatQuantityDivisor = int_to_float_quantity_divisor
        self.HasMarketDepthData = has_market_depth_data
        self.DisplayPriceMultiplier = display_price_multiplier
        self.ExchangeSymbol = exchange_symbol
        self.InitialMarginRequirement = initial_margin_requirement
        self.MaintenanceMarginRequirement = maintenance_margin_requirement
        self.Currency = currency
        self.ContractSize = contract_size
        self.OpenInterest = open_interest

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return SecurityDefinitionResponse(
             request_id=packet[0],
             symbol=packet[1],
             exchange=packet[2],
             security_type=packet[3],
             description=packet[4],
             min_price_increment=packet[5],
             price_display_format=packet[6],
             currency_value_per_increment=packet[7],
             is_final_message=packet[8],
             float_to_int_price_multiplier=packet[9],
             int_to_float_price_divisor=packet[10],
             underlying_symbol=packet[11],
             updates_bid_ask_only=packet[12],
             strike_price=packet[13],
             put_or_call=packet[14],
             short_interest=packet[15],
             security_expiration_date=packet[16],
             buy_rollover_interest=packet[17],
             sell_rollover_interest=packet[18],
             earnings_per_share=packet[19],
             shares_outstanding=packet[20],
             int_to_float_quantity_divisor=packet[21],
             has_market_depth_data=packet[22],
             display_price_multiplier=packet[23],
             exchange_symbol=packet[24],
             initial_margin_requirement=packet[25],
             maintenance_margin_requirement=packet[26],
             currency=packet[27],
             contract_size=packet[28],
             open_interest=packet[29]
        )

    @staticmethod
    def from_message_long(message_obj):
        return SecurityDefinitionResponse(
             request_id=message_obj.get('RequestID'),
             symbol=message_obj.get('Symbol'),
             exchange=message_obj.get('Exchange'),
             security_type=message_obj.get('SecurityType'),
             description=message_obj.get('Description'),
             min_price_increment=message_obj.get('MinPriceIncrement'),
             price_display_format=message_obj.get('PriceDisplayFormat'),
             currency_value_per_increment=message_obj.get('CurrencyValuePerIncrement'),
             is_final_message=message_obj.get('IsFinalMessage'),
             float_to_int_price_multiplier=message_obj.get('FloatToIntPriceMultiplier'),
             int_to_float_price_divisor=message_obj.get('IntToFloatPriceDivisor'),
             underlying_symbol=message_obj.get('UnderlyingSymbol'),
             updates_bid_ask_only=message_obj.get('UpdatesBidAskOnly'),
             strike_price=message_obj.get('StrikePrice'),
             put_or_call=message_obj.get('PutOrCall'),
             short_interest=message_obj.get('ShortInterest'),
             security_expiration_date=message_obj.get('SecurityExpirationDate'),
             buy_rollover_interest=message_obj.get('BuyRolloverInterest'),
             sell_rollover_interest=message_obj.get('SellRolloverInterest'),
             earnings_per_share=message_obj.get('EarningsPerShare'),
             shares_outstanding=message_obj.get('SharesOutstanding'),
             int_to_float_quantity_divisor=message_obj.get('IntToFloatQuantityDivisor'),
             has_market_depth_data=message_obj.get('HasMarketDepthData'),
             display_price_multiplier=message_obj.get('DisplayPriceMultiplier'),
             exchange_symbol=message_obj.get('ExchangeSymbol'),
             initial_margin_requirement=message_obj.get('InitialMarginRequirement'),
             maintenance_margin_requirement=message_obj.get('MaintenanceMarginRequirement'),
             currency=message_obj.get('Currency'),
             contract_size=message_obj.get('ContractSize'),
             open_interest=message_obj.get('OpenInterest')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return SecurityDefinitionResponse.from_message_short(message_obj)
        else:
            return SecurityDefinitionResponse.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "SecurityDefinitionResponse"
