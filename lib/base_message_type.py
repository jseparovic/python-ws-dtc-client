import json


class BaseMessageType:
    def to_JSON(self, pretty=False):
        def remove_nulls(d):
            return {k: v for k, v in d.items() if v is not None}

        indent = 4 if pretty else None
        res = json.loads(json.dumps(self, default=lambda o: o.__dict__), object_hook=remove_nulls)
        return json.dumps(res, sort_keys=True, indent=indent)
