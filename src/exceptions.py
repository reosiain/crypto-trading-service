
class ZeroObsException(Exception):
    """
    Raised when DB returns zero obs for a given query
    """
    pass


class NotEnoughData(Exception):
    """
    Raised when generator can't construct single full observation
    """
    pass


class ExchangeUnavailable(Exception):
    """
    OKX not responding
    """
    pass


class MarketBadSymbol(Exception):
    """
    Error in symbol
    """
    pass


class StaleDataException(Exception):
    """
    Couldn't fetch fresh data from db
    """
    pass
