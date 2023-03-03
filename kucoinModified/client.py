from kucoinModified.margin.margin import MarginData
from kucoinModified.market.market import MarketData
from kucoinModified.trade.trade import TradeData
from kucoinModified.user.user import UserData
from kucoinModified.ws_token.token import GetToken
from kucoinModified.isolatedMargin.isolatedMargin import IsolatedMarginData

class User(UserData):
    pass


class Trade(TradeData):
    pass


class Market(MarketData):
    pass


class Margin(MarginData):
    pass


class WsToken(GetToken):
    pass

class IsolatedMargin(IsolatedMarginData):
    pass


