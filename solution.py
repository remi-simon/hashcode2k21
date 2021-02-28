class Schedule:
    """Si possible on file à cette fonction un Schedule du type [(Street1, 5), (Street2, 3)]"""

    def __init__(self, intersection_id, E, schedule):
        self.intersection_id = intersection_id
        self.E = E
        self.schedule = schedule


class Solution:
    def __init__(self, number_of_intersection, intersections_schedule):
        self.A = number_of_intersection
        self.intersections_schedule = intersections_schedule

    def score(self, instance, points_per_car):
        return 0

    def convert_into_file(self, path):
        f = open(path, 'w')
        f.write(str(self.A)+"\n")
        for s in self.intersections_schedule:
            f.write(str(s.intersection_id)+"\n")
            f.write(str(len(s.schedule))+"\n")
            for x in s.schedule:
                # print(x)
                f.write(x[0]+" "+str(x[1])+"\n")
        f.close()
        return 0
