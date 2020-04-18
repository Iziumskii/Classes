class Animals:
    voice = 'voice'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        self.weight += 1


class Artiodactyls(Animals):
    def to_milk(self):
        self.weight -= 1


class Birds(Animals):
    def pick_eggs(self):
        self.weight -= 1
        pass


class Cow(Artiodactyls):
    voice = 'moo'


class Sheep(Artiodactyls):
    voice = 'baa'

    def to_cut(self):
        self.weight -= 2


class Goat(Artiodactyls):
    voice = 'bee'


class Duck(Birds):
    voice = 'quack'


class Goose(Birds):
    voice = 'honk'


class Hen(Birds):
    voice = 'cluck'


def animal_weight_add(animals_list, animal):
    animals_list.append(animal.weight)


def animal_animals_name_weight_add(animals_list, animal):
    animals_list.append([animal.name, animal.weight])


cow = Cow('Korova', 100)
sheep = Sheep('Ovca', 60)
goat = Goat('Koza', 40)
duck = Duck('Utka', 3)
goose = Goose('Gus', 5)
hen = Hen('Kurica', 3)

animal_list = [cow, sheep, goat, duck, goose, hen]
animals_weight_list = []
animals_name_weight_list = []

for animal in animal_list:
    animal_weight_add(animals_weight_list, animal)
    animal_animals_name_weight_add(animals_name_weight_list, animal)

print(f' Общий вес животных = {sum(animals_weight_list)}')

animals_name_weight_list.sort(key=lambda i: i[1])
print(f' Самое тяжёлое животное: {animals_name_weight_list[-1][0]}')
