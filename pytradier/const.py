# Constants for Tradier.com

API_ENDPOINT = {
    'sandbox':                  'sandbox.tradier.com',  # /v1/ paths
    'brokerage':                'api.tradier.com',      # /v1/ paths
    'stream':                   'stream.tradier.com',   # /v1/ paths
    'beta':                     'api.tradier.com'       # /beta/ paths
}


API_PATH = {

    # Authentication
        # to be implemented...

    # User Profile
    'profile':                  '/v1/user/profile',
    'balances':                 '/v1/user/balances',
    'positions':                '/v1/user/positions',
    'user_history':             '/v1/user/history',
    'gainloss':                 '/v1/user/gainloss',
    'user_orders':              '/v1/user/orders',

    # Market Data
    'quotes':                   '/v1/markets/quotes',
    'timesales':                '/v1/markets/timesales',
    'chains':                   '/v1/markets/options/chains',
    'strikes':                  '/v1/markets/options/strikes',
    'expirations':              '/v1/markets/options/expirations',
    'history':                  '/v1/markets/history',
    'clock':                    '/v1/markets/clock',
    'calendar':                 '/v1/markets/calendar',
    'search':                   '/v1/markets/search',
    'lookup':                   '/v1/markets/lookup',
    'stream':                   '/v1/markets/events/session',

    # Trading
    'orders':                   '/v1/accounts/{account_id}/orders',

    # Fundementals
    'company':                  '/beta/markets/fundamentals/company',
    'corporate_calendars':      '/beta/markets/fundamentals/calendars',
    'dividends':                '/beta/markets/fundamentals/dividends',
    'corporate_actions':        '/beta/markets/fundamentals/corporate_actions',
    'ratios':                   '/beta/markets/fundamentals/ratios',
    'financials':               '/beta/markets/fundamentals/financials',
    'statistics':               '/beta/markets/fundamentals/statistics',

    # Watchlists
    'watchlist':                '/v1/watchlists',
    'watchlist_id':             '/watchlists/{id}',
    'watchlist_add_symbols':    '/v1/watchlists/{id}/symbols',
    'watchlist_remove_symbols': '/v1/watchlists/{id}/symbols/{symbol}',
    
    # Streaming
    'stream_quote':             '/v1/markets/events'
}



EXCHANGE_CODES = {
    'A':                        'NYSE MKT',
    'B':                        'NASDAQ OMX BX',
    'C':                        'National Stock Exchange',
    'D':                        'FINRA ADF',
    'E':                        'Market Independent (Generated by Nasdaq SIP)',
    'F':                        'Mutual Funds/Money Markets (NASDAQ)',
    'G':                        'GLOBEX',
    'I':                        'International Securities Exchange',
    'J':                        'Direct Edge A',
    'K':                        'Direct Edge X',
    'M':                        'Chicago Stock Exchange',
    'N':                        'NYSE',
    'P':                        'NYSE Arca',
    'Q':                        'NASDAQ OMX',
    'S':                        'NASDAQ Small Cap',
    'T':                        'NASDAQ Int',
    'U':                        'OTCBB',
    'V':                        'OTC other',
    'W':                        'CBOE',
    'X':                        'NASDAQ OMX PSX',
    'Y':                        'BATS Y-Exchange',
    'Z':                        'BATS'
}


OPRA_FEEDS = {
    'A':                        'NYSE Amex Options',
    'B':                        'BOX Options Exchange',
    'C':                        'Chicago Board Options Exchange (CBOE)',
    'H':                        'ISE Gemini',
    'I':                        'International Securities Exchange (ISE)',
    'M':                        'MIAX Options Exchange',
    'N':                        'NYSE Arca Options',
    'O':                        'Options Price Reporting Authority (OPRA)',
    'P':                        'MIAX PEARL',
    'Q':                        'NASDAQ Options Market',
    'T':                        'NASDAQ OMX BX',
    'W':                        'C2 Options Exchange',
    'X':                        'NASDAQ OMX PHLX',
    'Z':                        'BATS Options Market'
}

