#coding:utf-8

import random


class DataException(BaseException):
    def __init__(self):
        super(DataException, self).__init__()

    def well(self):
        pass


class GeneticalOptimizer(object):
    def __init__(self,
                 initial_population,
                 weight_function,
                 breeding_function,
                 unit_breeds=2):

        super(GeneticalOptimizer, self).__init__()
        if len(initial_population) < 2:
            raise DataException("Not enough unit to breed.")

        self.weight_function = weight_function
        self.breeding_function = breeding_function
        self.initial_population = initial_population
        self.population = [unit for unit in self.initial_population
                           if self.weight_function(unit) > 0]
        self.unit_breeds = unit_breeds

    def breed(self):
        parents = [choice(self.population, self.weight_function)
                   for i in range(self.unit_breeds)]

        child = self.breeding_function(parents)
        if self.weight_function(child) > 0:
            if child not in self.population:
                self.population.append(child)

    def generate(self, count=None, natural_selection=None):
        if not count:
            count = random.randrange(0, len(self.population))
        for _ in range(count):
            self.breed()

        if isinstance(natural_selection, int):
            sorted_pop = sorted(self.population, key=self.weight_function)
            self.population = sorted_pop[:natural_selection]

    def fittest(self):
        return max(self.population, key=self.weight_function)


def choice(bundle, weight_key=lambda x: 1, with_index=False):
    cumulative_list = [0]
    summation = 0
    for element in bundle:
        summation += weight_key(element)
        cumulative_list.append(summation)

    random_num = random.random() * float(summation)
    i = 0
    while cumulative_list[i] < random_num:
        i += 1
    if with_index:
        return {'value': bundle[i-1], 'index': i-1}
    return bundle[i-1]


def shuffle(bundle, weight_key=lambda x: 1):
    badcopy = bundle[:]
    result = []
    while badcopy:
        choosen_one = choice(bundle=badcopy, weight_key=weight_key,
                             with_index=True)
        result.append(choosen_one['value'])
        badcopy.pop(choosen_one['index'])
    return result


def sample(bundle, size=None, weight_key=lambda x: 1):
    if not size:
        size = random.randrange(len(bundle))
    badcopy = bundle[:]
    result = []
    for i in range(size):
        choosen_one = choice(bundle=badcopy, weight_key=weight_key,
                             with_index=True)
        result.append(choosen_one['value'])
        badcopy.pop(choosen_one['index'])
    return result
