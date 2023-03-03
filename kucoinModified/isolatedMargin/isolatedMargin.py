from kucoinModified.base_request.base_request import KucoinBaseRestApi


class IsolatedMarginData(KucoinBaseRestApi):

    # def get_mark_price(self, symbol):
    #     """
    #     https://docs.kucoin.com/#margin-info
    #     :param symbol: symbol (Mandatory)
    #     :type: str
    #     :return:
    #     {
    #         "symbol": "USDT-BTC",
    #         "granularity": 5000,
    #         "timePoint": 1568701710000,
    #         "value": 0.00009807
    #     }
    #     """
    #     return self._request('GET', '/api/v1/mark-price/{symbol}/current'.format(symbol=symbol))

    # def get_margin_config(self):
    #     """
    #     https://docs.kucoin.com/#get-margin-configuration-info
    #     :return:
    #     {
    #         "currencyList": ["BTC","USDT","EOS"],
    #         "warningDebtRatio": "0.8",
    #         "liqDebtRatio": "0.9",
    #         "maxLeverage": "3"
    #     }
    #     """
    #     return self._request('GET', '/api/v1/margin/config')

    # def get_margin_account(self):
    #     """
    #     https://docs.kucoin.com/#get-margin-account
    #     :return:
    #     {
    #         "accounts": [
    #           {
    #             "availableBalance": "990.11",
    #             "currency": "USDT",
    #             "holdBalance": "7.22",
    #             "liability": "66.66",
    #             "maxBorrowSize": "88.88",
    #             "totalBalance": "997.33"
    #           }
    #         ],
    #         "debtRatio": "0.33"
    #     }
    #     """
    #     return self._request('GET', '/api/v1/margin/account')

    def get_single_isolated_margin_account(self, symbol, **kwargs):
        """
        https://docs.kucoin.com/#query-isolated-margin-account-info
        :return:
        {
            "code": "200000",
            "data": {
                "symbol": "MANA-USDT",
                "status": "CLEAR",
                "debtRatio": "0",
                "baseAsset": {
                    "currency": "MANA",
                    "totalBalance": "0",
                    "holdBalance": "0",
                    "availableBalance": "0",
                    "liability": "0",
                    "interest": "0",
                    "borrowableAmount": "0"
                },
                "quoteAsset": {
                    "currency": "USDT",
                    "totalBalance": "0",
                    "holdBalance": "0",
                    "availableBalance": "0",
                    "liability": "0",
                    "interest": "0",
                    "borrowableAmount": "0"
                }
            }
        }
        """

        return self._request('GET', '/api/v1/isolated/account/{symbol}'.format(symbol=symbol))

    # def create_borrow_order(self, currency, order_type, size, **kwargs):
    #     """
    #     https://docs.kucoin.com/#post-borrow-order
    #     :param currency: Currency to Borrow (Mandatory)
    #     :type: str
    #     :param order_type: Type: FOK, IOC (Mandatory)
    #     :type: str
    #     :param size: Total size (Mandatory)
    #     :type: float
    #     :param kwargs: [Optional] maxRate, term
    #     :return:
    #     {
    #         "orderId": "a2111213",
    #         "currency": "USDT"
    #     }
    #     """
    #     params = {
    #         'currency': currency,
    #         'type': order_type,
    #         'size': size,
    #     }
    #     if kwargs:
    #         params.update(kwargs)
    #     return self._request('POST', '/api/v1/margin/borrow', params=params)

    def create_borrow_order_isolated_margin(self, symbol, currency, size, borrowStrategy, **kwargs):
        """
        https://docs.kucoin.com/#isolated-margin-borrowing
        Param	        Type	    Mandatory	Description
        symbol	        String	    Yes	        Trading pair, e.g.: BTC-USDT
        currency	    String	    Yes	        Borrowed coin type
        size	        BigDecimal	Yes	        Borrowed amount
        borrowStrategy	String	    Yes	        Borrowing strategy: FOK, IOC
        maxRate	        BigDecimal	No	        Max interest rate, defaults to all interest rates if left blank
        period	        String	    No	        The term in days. Defaults to all terms if left blank. 7,14,28

        :return:
        {
            "code": "200000",
            "data": {
                "orderId": "62baad0aaafc8000014042b3",
                "currency": "USDT",
                "actualSize": "10"
            }
        }
        """
        params = {
            'symbol': symbol,
            'currency': currency,
            'size': size,
            'borrowStrategy': borrowStrategy,
        }
        if kwargs:
            params.update(kwargs)
        return self._request('POST', '/api/v1/isolated/borrow', params=params)

    # def get_borrow_order(self, orderId):
    #     """
    #     https://docs.kucoin.com/#get-borrow-order
    #     :param orderId: Borrow order ID
    #     :type: str
    #     :return:
    #     {
    #         "currency": "USDT",
    #         "filled": 1.009,
    #         "matchList": [
    #           {
    #             "currency": "USDT",
    #             "dailyIntRate": "0.001",
    #             "size": "12.9",
    #             "term": 7,
    #             "timestamp": "1544657947759",
    #             "tradeId": "1212331"
    #           }
    #         ],
    #         "orderId": "a2111213",
    #         "size": "1.009",
    #         "status": "DONE"
    #       }
    #     """
    #     params = {
    #         'orderId': orderId
    #     }

    #     return self._request('GET', '/api/v1/margin/borrow', params=params)

    # def get_repay_record(self, **kwargs):
    #     """
    #     https://docs.kucoin.com/#get-repay-record
    #     :param kwargs: [Optional] currency, currentPage, pageSize
    #     :return:
    #     {
    #         "currentPage": 0,
    #         "items": [
    #           {
    #             "accruedInterest": "0.22121",
    #             "createdAt": "1544657947759",
    #             "currency": "USDT",
    #             "dailyIntRate": "0.0021",
    #             "liability": "1.32121",
    #             "maturityTime": "1544657947759",
    #             "principal": "1.22121",
    #             "repaidSize": "0",
    #             "term": 7,
    #             "tradeId": "1231141"
    #           }
    #         ],
    #         "pageSize": 0,
    #         "totalNum": 0,
    #         "totalPage": 0
    #       }
    #     """
    #     params = {}
    #     if kwargs:
    #         params.update(kwargs)
    #     return self._request('GET', '/api/v1/margin/borrow/outstanding', params=params)

    # def get_repayment_record(self, **kwargs):
    #     """
    #     https://docs.kucoin.com/#get-repayment-record
    #     :param kwargs: [Optional] currency, currentPage, pageSize
    #     :return:
    #     {
    #         "currentPage": 0,
    #         "items": [
    #           {
    #             "currency": "USDT",
    #             "dailyIntRate": "0.0021",
    #             "interest": "0.22121",
    #             "principal": "1.22121",
    #             "repaidSize": "0",
    #             "repayTime": "1544657947759",
    #             "term": 7,
    #             "tradeId": "1231141"
    #           }
    #         ],
    #         "pageSize": 0,
    #         "totalNum": 0,
    #         "totalPage": 0
    #       }
    #     """
    #     params = {}
    #     if kwargs:
    #         params.update(kwargs)
    #     return self._request('GET', '/api/v1/margin/borrow/repaid', params=params)

    # def click_to_repayment(self, currency, sequence, size):
    #     """
    #     https://docs.kucoin.com/#one-click-repayment
    #     :param currency: currency (Mandatory)
    #     :type: str
    #     :param sequence: Repayment strategy. (Mandatory)
    #     RECENTLY_EXPIRE_FIRST: Time priority, namely to repay the loans of the nearest maturity time first,
    #     HIGHEST_RATE_FIRST: Rate Priority: Repay the loans of the highest interest rate first.
    #     :type: str
    #     :param size: Repayment size (Mandatory)
    #     :type: float
    #     :return:
    #     """
    #     params = {
    #         'currency': currency,
    #         'sequence': sequence,
    #         'size': size
    #     }
    #     return self._request('POST', '/api/v1/margin/repay/all', params=params)

    def click_to_repayment_isolated_margin(self, symbol, currency, size, seqStrategy):
        """
        https://docs.kucoin.com/#query-repayment-records
        :param symbol: Trading pair, e.g.: BTC-USDT
        :type: str
        :param currency: currency (Mandatory)
        :type: str
        :param sequence: Repayment strategy. (Mandatory)
        RECENTLY_EXPIRE_FIRST: Time priority, namely to repay the loans of the nearest maturity time first,
        HIGHEST_RATE_FIRST: Rate Priority: Repay the loans of the highest interest rate first.
        :type: str
        :param size: Repayment size (Mandatory)
        :type: float
        :return:
        """
        params = {
            'symbol': symbol,
            'currency': currency,
            'size': size,
            'seqStrategy': seqStrategy
        }
        return self._request('POST', '/api/v1/isolated/repay/all', params=params)

    # def repay_single_order(self, currency, tradeId, size):
    #     """
    #     https://docs.kucoin.com/#repay-a-single-order
    #     :param currency: currency (Mandatory)
    #     :type: str
    #     :param tradeId: Trade ID (Mandatory)
    #     :type: str
    #     :param size: Repayment size (Mandatory)
    #     :type: float
    #     :return:
    #     """
    #     params = {
    #         'currency': currency,
    #         'tradeId': tradeId,
    #         'size': size
    #     }
    #     return self._request('POST', '/api/v1/margin/repay/single', params=params)

    # def get_active_order(self, **kwargs):
    #     """
    #     https://docs.kucoin.com/#get-active-order
    #     :param kwargs: [Optional] currency, currentPage, pageSize
    #     :return:
    #     {
    #         "currentPage": 1,
    #         "pageSize": 1,
    #         "totalNum": 1,
    #         "totalPage": 1,
    #         "items": [{
    #             "orderId": "5da59f5ef943c033b2b643e4",
    #             "currency": "BTC",
    #             "size": "0.51",
    #             "filledSize": "0",
    #             "dailyIntRate": "0.0001",
    #             "term": 7,
    #             "createdAt": 1571135326913
    #         }]
    #     }
    #     """
    #     params = {}
    #     if kwargs:
    #         params.update(kwargs)
    #     return self._request('GET', '/api/v1/margin/lend/active', params=params)

    # def get_active_list(self, **kwargs):
    #     """
    #     https://docs.kucoin.com/#get-active-lend-order-list
    #     :param kwargs: [Optional] currency, currentPage, pageSize
    #     :return:
    #     {
    #         "currentPage": 1,
    #         "pageSize": 1,
    #         "totalNum": 1,
    #         "totalPage": 1,
    #         "items": [{
    #             "tradeId": "5da6dba0f943c0c81f5d5db5",
    #             "currency": "BTC",
    #             "size": "0.51",
    #             "accruedInterest": "0",
    #             "repaid": "0.10999968",
    #             "dailyIntRate": "0.0001",
    #             "term": 14,
    #             "maturityTime": 1572425888958
    #         }]
    #     }
    #     """
    #     params = {}
    #     if kwargs:
    #         params.update(kwargs)
    #     return self._request('GET', '/api/v1/margin/lend/trade/unsettled', params=params)

    # def get_settled_order(self, **kwargs):
    #     """
    #     https://docs.kucoin.com/#get-settled-lend-order-history
    #     :param kwargs: [Optional] currency, currentPage, pageSize
    #     :return:
    #     {
    #         "currentPage": 1,
    #         "pageSize": 1,
    #         "totalNum": 1,
    #         "totalPage": 1,
    #         "items": [{
    #             "tradeId": "5da59fe6f943c033b2b6440b",
    #             "currency": "BTC",
    #             "size": "0.51",
    #             "interest": "0.00004899",
    #             "repaid": "0.510041641",
    #             "dailyIntRate": "0.0001",
    #             "term": 7,
    #             "settledAt": 1571216254767,
    #             "note": "The account of the borrowers reached a negative balance, and the system has supplemented the loss via the insurance fund. Deposit funds: 0.51."
    #         }]
    #     }
    #     """
    #     params = {}
    #     if kwargs:
    #         params.update(kwargs)
    #     return self._request('GET', '/api/v1/margin/lend/trade/settled', params=params)

    # def get_margin_data(self, currency):
    #     """
    #     https://docs.kucoin.com/#margin-trade-data
    #     :param currency: currency (Mandatory)
    #     :type: str
    #     :return:
    #     [{
    #         "tradeId": "5da6dba0f943c0c81f5d5db5",
    #         "currency": "BTC",
    #         "size": "0.51",
    #         "dailyIntRate": "0.0001",
    #         "term": 14,
    #         "timestamp": 1571216288958989641
    #     }]
    #     """
    #     params = {
    #         'currency': currency
    #     }
    #     return self._request('GET', '/api/v1/margin/trade/last', params=params)
