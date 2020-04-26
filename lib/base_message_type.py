import json

USERNAME = 'Username'
PASSWORD = 'Password'
TRADE_ACCOUNT = 'TradeAccount'
STARS = "********"


class BaseMessageType:
    def to_JSON(self, pretty=False, logging=True):
        def remove_nulls(d):
            return {k: v for k, v in d.items() if v is not None}

        indent = 4 if pretty else None
        res = json.loads(json.dumps(self, default=lambda o: o.__dict__), object_hook=remove_nulls)
        # mask some sensitive values
        if logging:
            #if USERNAME in res:
            #    res[USERNAME] = STARS
            if PASSWORD in res:
                res[PASSWORD] = STARS
            #if TRADE_ACCOUNT in res:
            #    res[TRADE_ACCOUNT] = STARS
        return json.dumps(res, sort_keys=True, indent=indent)
