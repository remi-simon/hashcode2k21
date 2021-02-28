# Sur l'instance de l'an dernier, le séparateur était un espace, tu peux ptêtre préparer la ligne
# qui split selon les espaces

class Car:
    def __init__(self, id, itinerary):
        self.id = id
        self.itinerary = itinerary


class Street:
    """Chaque rue a un couple d'intersection type (1,3) et une durée L"""

    def __init__(self, intersections, duration, id, name):
        self.id = id
        self.intersections = intersections
        self.L = duration
        self.name = name


class Intersection:
    """ streets_in contient la liste des rues entrantes, compute_frequency"""

    def __init__(self, id, streets_in, streets_out):
        self.id = id
        self.streets_in = streets_in
        self.streets_out = streets_out
        self.cycle_duration = len(streets_in)

    def compute_frequency(self, instance):
        self.frequency = [0]*len(self.streets_in)
        nb_car = 0
        for idx in range(len(self.streets_in)):
            for car in instance.cars:
                if self.streets_in[idx] in car.itinerary:
                    self.frequency[idx] += 1
                    nb_car += 1
        if nb_car != 0:
            self.frequency = [freq/nb_car for freq in self.frequency]
        else:
            self.frequency = [1/len(self.streets_in)
                              for freq in self.frequency]

    def compute_schedule(self):
        schedule = []
        for i in range(len(self.streets_in)):
            if self.frequency[i] != 0:
                schedule.append((self.streets_in[i].name, max(
                    int(self.frequency[i]*self.cycle_duration), 1)))
        return schedule


class Instance:
    def __init__(self, D, I, S, V, F, streets, cars):
        self.D = D
        self.I = I
        self.S = S
        self.V = V
        self.F = F
        self.streets = streets
        self.cars = cars
        self.intersections = []
        print("en train de créer les intersections")
        for i in range(I):
            self.intersections.append(Intersection(i, [], []))
        for name in streets:
            self.intersections[streets[name].intersections[1]
                               ].streets_in.append(streets[name])
            self.intersections[streets[name].intersections[0]
                               ].streets_out.append(streets[name])
        print("fini de créer les intersections")

    def affiche(self):
        print(self.D, self.I, self.S, self.V, self.F)
        for street in self.streets:
            print("Rue n°" + str(street.id),
                  street.intersections, street.L, street.name)
        for car in self.cars:
            print("Voiture n°" + str(car.id))
            for street in car.itinerary:
                print(street.id, street.intersections, street.L, street.name)
        for intersec in self.intersections:
            print("Intersection n°" + str(intersec.id))
            print("Streets in :")
            for street in intersec.streets_in:
                print(street.name)
            print("Streets out :")
            for street in intersec.streets_out:
                print(street.name)


def convert_street_name_into_street(name, streets):
    for street in streets:
        if street.name == name:
            return street
    return Street([], 0, -1, '')


def read_instance(path):
    instance = open(path, "r")
    lines = instance.readlines()
    first_line = lines[0].split(' ')
    simulation_duration = int(first_line[0])
    number_of_intersection = int(first_line[1])
    number_of_streets = int(first_line[2])
    number_of_cars = int(first_line[3])
    bonus_points = int(first_line[4])
    streets_list = {}
    # streets_list = []
    id_street = 0
    print("en train de lire les rues")
    for line in lines[1:1+number_of_streets]:
        tab = line.split(' ')
        #streets_list.append(Street((int(tab[0]), int(tab[1])), int(tab[3]), id_street, tab[2]))
        streets_list[tab[2]] = Street(
            (int(tab[0]), int(tab[1])), int(tab[3]), id_street, tab[2])
        id_street += 1

    cars_list = []
    id_car = 0
    print("en train de lire les voitures")
    for line in lines[1+number_of_streets:1+number_of_streets+number_of_cars]:
        tab = line.split(' ')
        itinerary_with_names = [x.rstrip() for x in tab[1:]]
        cars_list.append(
            Car(id_car, [streets_list[name]
                         for name in itinerary_with_names])
        )
        id_car += 1
    print("fini de lire les voitures")

    final_instance = Instance(simulation_duration, number_of_intersection,
                              number_of_streets, number_of_cars, bonus_points, streets_list, cars_list)
    # final_instance.affiche()
    return final_instance


# inst = read_instance("./instance/a.txt")

# moyenneL = 0
# for street in inst.streets:
#    moyenneL += street.L
# moyenneL = moyenneL/len(street)
