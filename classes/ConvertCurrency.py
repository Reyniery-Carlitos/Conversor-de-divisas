from lark import Lark, Transformer
from lark.tree import Tree

from helpers.conversionRates import conversionRates
from helpers.conversionGrammar import conversionGrammar

class ConvertCurrency(Transformer):
    def start(self, items):
        amount = float(items[0])
        fromCurrency = items[1].upper()
        toCurrency = items[2].upper()
        rate = conversionRates[fromCurrency]['exchange'][toCurrency]
        convertedAmount = amount * rate
        tree = Tree('conversion', [Tree('amount', [amount]), Tree('fromCurrency', [fromCurrency]), Tree('toCurrency', [toCurrency]), Tree('convertedAmount', [convertedAmount])])
        return tree

conversionParser = Lark(conversionGrammar, parser='lalr', transformer=ConvertCurrency())
convertCurrency = conversionParser.parse