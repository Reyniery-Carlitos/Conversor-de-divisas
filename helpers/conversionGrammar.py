conversionGrammar = """
    ?start: AMOUNT CURRENCY "to" CURRENCY
          | AMOUNT CURRENCY "TO" CURRENCY
          | AMOUNT CURRENCY "a" CURRENCY
          | AMOUNT CURRENCY "A" CURRENCY

    AMOUNT: /[0-9]+(\.[0-9]+)?/
    CURRENCY: /[A-Za-z]{3}/

    %import common.WS_INLINE
    %ignore WS_INLINE
"""