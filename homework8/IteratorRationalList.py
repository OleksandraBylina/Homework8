from Rational import Rational
from Rational import Integer
class IteratorRationalList:
    def __init__(self, list_of_numbers): #предположим, что оно принимает сплитнутые строки
        self.list_of_numbers = list_of_numbers.list_of_numbers
        self.list_of_numbers.sort()
        # self.list_of_numbers.reverse()
        self.index = 0
    def __next__(self):
        try:
            result = self.list_of_numbers[self.index]
            self.index += 1
            return result
        except IndexError:
            raise StopIteration


