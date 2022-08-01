class FractionError(Exception):
    pass


class NullDenomiatorException(FractionError):
    pass


class ParameterIsNotAFractionException(FractionError):
    pass


class Fraction:
    def __init__(self, numerator, denominator):
        pass

    def value(self):
        pass

    def get_numerator(self):
        pass

    def get_denominator(self):
        pass

    def is_equal(self, fraction_to_evaluate):
        pass
