import hashlib


def get_symbol_id(symbol):
    return int(hashlib.sha1(symbol.encode('utf-8')).hexdigest(), 16) % 4294967295