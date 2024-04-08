from Rational import Integer
from Rational import Rational
from IteratorRationalList import IteratorRationalList
class RationalList:
    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers
    def  __getitem__(self, index):
        assert index < len(self.list_of_numbers)
        return self.list_of_numbers[index]

    def __setitem__(self, index, value):
        self.list_of_numbers[index] = value
    def __len__(self):
        return len(self.list_of_numbers)
    def __iadd__(self, other):
        if type (other) == Rational:
            self.list_of_numbers.append(Rational(other))
        elif type(other) == Integer:
            self.list_of_numbers.append(Integer(other))
        elif type (other) == RationalList:
            for i in other:
                if type(i) == Rational:
                    self.list_of_numbers.append(Rational(i))
                elif type(i) == Integer:
                    self.list_of_numbers.append(Integer(i))
        return self.list_of_numbers
    def __add__(self, other):
        new_list = []
        for i in self.list_of_numbers:
            if type(i) == Rational:
                new_list.append(Rational(i))
            elif type(i) == Integer:
                new_list.append(Integer(i))
        if type (other) == Rational:
            new_list.append(Rational(other))
        elif type(other) == Integer:
            new_list.append(Integer(other))
        elif type (other) == RationalList:
            for i in other:
                if type(i) == Rational:
                    new_list.append(Rational(i))
                elif type(i) == Integer:
                    new_list.append(Integer(i))
        return new_list
    def __iter__(self):
        return IteratorRationalList(self)

if __name__ == "__main__":
    #lst = [Rational("55/4"), Rational("5/1"), Rational("55/44"), Rational("767/2"), Rational("62/44")]
    #r = RationalList(lst)
    #for el in r:
        #print(el)
    data_collector = []
    data_collector_integer = []
    with open("input02.txt") as f:
        for line in f:
            data = line.split()
            for i in data:
                if "/" in i:
                    data_collector.append(Rational(i))
            for r in data:
                if "/" not in r:
                    data_collector_integer.append(Integer(r))
    m = RationalList(data_collector)
    n = RationalList(data_collector_integer)
    for el in m:
        print(el)
    for en in n:
        print (en)


    # total_results = []
    # with open("input02.txt") as f:
    #     for line in f:
    #         data = line.split()
    #         while data:
    #             try:
    #                 if "/" in data[0] and "/" in data[1]:
    #                     new = Rational(data[0]) + Rational(data[1])
    #                     data[0] = f"{new}"
    #                     del data[1]
    #                 elif "/" not in data[0] and not "/" in data[1]:
    #                     new = Integer(data[0]) + Integer(data[1])
    #                     data[0] = f"{new}"
    #                     del data[1]
    #                 elif "/" in data[0] and "/" not in data[1]:
    #                     new = Rational(data[0]) + Integer(data[1])
    #                     data[0] = f"{new}"
    #                     del data[1]
    #                 elif "/" not in data[0] and "/" in data[1]:
    #                     new = Rational(data[1]) + Integer(data[0])
    #                     data[0] = f"{new}"
    #                     del data[1]
    #             except IndexError:
    #                 break
    #         #print(*data)
    #         total_results += data
    #
    # with open("input02.txt") as f:
    #     for line in f:
    #         data = line.split()
    #
    #         r = IteratorRationalList(data)
    #         #while data:
    #         for i in r:
    #             print(i)
    # # #print(*total_result