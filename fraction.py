class FractionError(Exception):
    pass


class Fraction:
    numerator = 0;
    denominator = 0;

    def __init__(self, numerator=1, denominator=1):
        if denominator == 0:
            raise FractionError
        self.numerator = numerator
        self.denominator = denominator

    def value(self):
        return self.numerator / self.denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
