
class FractionError(Exception):
    pass


class NullDenominatorException(FractionError):
    pass


class ParameterIsNotAFractionException(FractionError):
    pass


class Fraction:

    numerator = 0
    denominator = 0

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def get_value(self):
        pass

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def is_equal(self, fraction_to_evaluate):
        pass
