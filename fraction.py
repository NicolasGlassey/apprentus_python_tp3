class FractionError(Exception):
    pass


class NullDenominatorException(FractionError):
    pass


class ParameterIsNotAFractionException(FractionError):
    pass


class Fraction:

    def __init__(self, numerator = 1, denominator = 1):
        pass

    def value(self):
        pass

    def get_numerator(self):
        pass

    def get_denominator(self):
        pass

    def is_equal(self, fraction_to_evaluate):
        pass
