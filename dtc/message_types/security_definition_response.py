
import json
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

