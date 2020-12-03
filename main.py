class Goose:

    def __init__(self, name, weight, agg=0):
        self.name = name
        self.weight = weight
        self.hungry = True
        self.voice = False
        self.agg = agg

    def add_in_list(self, list):
        list.append(self)

    def let_eat(self, view_eat, volume_eat):
        self.weight += volume_eat
        if view_eat == "Корм" and volume_eat > 150:
            self.hungry = True
        else:
            self.hungry = False

    def send_agg(self, hour):
        self.agg += hour

    def voice_which(self, view_voice):
        if view_voice == "Га-га":
            voice = True
        else:
            voice = False


class Cow:

    def __init__(self, name, weight, volume_milk=0):
        self.name = name
        self.weight = weight
        self.hungry = True
        self.voice = False
        self.volume_milk = volume_milk

    def add_in_list(self, list):
        list.append(self)

    def let_eat(self, view_eat, volume_eat):
        self.weight += volume_eat
        if view_eat == "Сено" and volume_eat > 1000:
            self.hungry = True
        else:
            self.hungry = False

    def send_milk(self, hour):
        self.volume_milk += hour

    def voice_which(self, view_voice):
        if view_voice == "Му-Му":
            voice = True
        else:
            voice = False


class Sheep:
    def __init__(self, name, weight, volume_wool=0):
        self.name = name
        self.weight = weight
        self.hungry = True
        self.voice = False
        self.volume_wool = volume_wool

    def add_in_list(self, list):
        list.append(self)

    def let_eat(self, view_eat, volume_eat):
        if view_eat == "Graas" and volume_eat > 300:
            self.hungry = True
        else:
            self.hungry = False

    def send_wool(self, hour):
        self.volume.wool += hour

    def voice_which(self, view_voice):
        if view_voice == "Бе-бе":
            voice = True
        else:
            voice = False


class Chiken:

    def __init__(self, name, weight, agg=0):
        self.name = name
        self.weight = weight
        self.hungry = True
        self.voice = False
        self.agg = agg

    def add_in_list(self, list):
        list.append(self)

    def let_eat(self, view_eat, volume_eat):
        if view_eat == "Graas" and volume_eat > 100:
            self.hungry = True
        else:
            self.hungry = False

    def send_agg(self, hour):
        self.agg += hour

    def voice_which(self, view_voice):
        if view_voice == "Ку-ка-ре-ку":
            voice = True
        else:
            voice = False


class Goat:

    def __init__(self, name, weight, volume_milk=0):
        self.name = name
        self.weight = weight
        self.hungry = True
        self.voice = True
        self.volume_milk = volume_milk

    def add_in_list(self, list):
        list.append(self)

    def let_eat(self, view_eat, volume_eat):
        if view_eat == "Hay" and volume_eat > 500:
            self.hungry = True
        else:
            self.hungry = False

    def send_milk(self, hour):
        self.volume_milk += hour

    def voice_of_animal(self, view_voice):
        if view_voice == "Ме":
            voice = True
        else:
            voice = False


class Duck:

    def __init__(self, name, weight, agg=0):
        self.name = name
        self.weight = weight
        self.hungry = True
        self.voice = False
        self.agg = agg

    def add_in_list(self, list):
        list.append(self)

    def let_eat(self, view_eat, volume_eat):
        if view_eat == "Graas" and volume_eat > 100:
            self.hungry = True
        else:
            self.hungry = False

    def send_agg(self, hour):
        self.agg += hour

    def voice_of_animal(self, view_voice):
        if view_voice == "Кря-кря":
            voice = True
        else:
            voice = False


animals_goose = []
animals_cow = []
animals_sheep = []
animals_chiken = []
animals_goat = []
animals_duck = []
animals = []

goose_1 = Goose("Серый", 25)
goose_2 = Goose("Белый", 40)
goose_1.add_in_list(animals_goose)
goose_2.add_in_list(animals_goose)
animals.append(goose_1)
animals.append(goose_2)
cow_1 = Cow("Манька", 150)
cow_1.add_in_list(animals_cow)
animals.append(cow_1)
sheep_1 = Sheep("Барашек", 85)
sheep_2 = Sheep("Кудрявый", 78)
sheep_1.add_in_list(animals_sheep)
sheep_2.add_in_list(animals_sheep)
animals.append(sheep_1)
animals.append(sheep_2)
chiken_1 = Chiken("Коко", 34)
chiken_2 = Chiken("Кукуреку", 20)
chiken_1.add_in_list(animals_chiken)
chiken_2.add_in_list(animals_chiken)
animals.append(chiken_1)
animals.append(chiken_2)
goat_1 = Goat("Рога", 50)
goat_2 = Goat("Копыта", 45)
goat_1.add_in_list(animals_goat)
goat_2.add_in_list(animals_goat)
animals.append(goat_1)
animals.append(goat_2)
duck_1 = Duck("Кряква", 29)
duck_1.add_in_list(animals_duck)
animals.append(duck_1)
print(animals)
weight_all_goose = sum(element.weight for element in animals_goose)
print("Общий вес гусей на ферме:", weight_all_goose, "кг")
weight_all_cow = sum(element.weight for element in animals_cow)
print("Общий вес коров на ферме:", weight_all_cow, "кг")
weight_all_sheep = sum(element.weight for element in animals_sheep)
print("Общий вес овец на ферме:", weight_all_sheep, "кг")
weight_all_chiken = sum(element.weight for element in animals_chiken)
print("Общий вес куриц на ферме:", weight_all_sheep, "кг")
weight_all_goat = sum(element.weight for element in animals_goat)
print("Общий вес коз на ферме:", weight_all_goat, "кг")
weight_all_duck = sum(element.weight for element in animals_duck)
print("Общий вес уток на ферме:", weight_all_duck, "кг")
max_weight = max(element.weight for element in animals_goose)
for element in animals_goose:
    if max_weight == element.weight:
        print("Самый тяжелый гусь:", element.name)
max_weight = max(element.weight for element in animals_cow)
print(max_weight)
for element in animals_cow:
    if max_weight == element.weight:
        print("Самая тяжелая корова:", element.name)
max_weight = max(element.weight for element in animals_sheep)
print(max_weight)
for element in animals_sheep:
    if max_weight == element.weight:
        print("Самая тяжелая овца:", element.name)
max_weight = max(element.weight for element in animals_chiken)
print(max_weight)
for element in animals_chiken:
    if max_weight == element.weight:
        print("Самая тяжелая курица:", element.name)
max_weight = max(element.weight for element in animals_goat)
print(max_weight)
for element in animals_goat:
    if max_weight == element.weight:
        print("Самая тяжелая коза:", element.name)
max_weight = max(element.weight for element in animals_duck)
print(max_weight)
for element in animals_duck:
    if max_weight == element.weight:
        print("Самая тяжелая утка:", element.name)

