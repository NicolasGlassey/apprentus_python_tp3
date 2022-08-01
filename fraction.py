class FractionError(Exception):
    pass


class NullDenominatorException(FractionError):
    pass


class ParameterIsNotAFractionException(FractionError):
    pass


class Fraction:

    numerator = 0
    denominator = 0

    def __init__(self, numerator = 1, denominator = 1):
        if denominator == 0:
            raise NullDenominatorException()
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def value(self):
        return self.numerator / self.denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def is_equal(self, fraction_to_evaluate):
        if not isinstance(fraction_to_evaluate, Fraction):
            raise ParameterIsNotAFractionException()
        return self.value() == fraction_to_evaluate.value()
