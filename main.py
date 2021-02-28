# on va gagner

from parse import *
from solution import *

green_mean_time = 1.5
for inst in ["a", "b", "c", "e", "f"]:
    # for inst in ["a"]:
    instance_path = "./instance/"+inst+".txt"
    instance = read_instance(instance_path)
    schedules = []
    print(inst)
    compteur = 0
    for intersection in instance.intersections:
        compteur += 1
        if compteur % 1000 == 0:
            print('compteur ', compteur)
        intersection.cycle_duration = len(
            intersection.streets_in)*green_mean_time
        intersection.compute_frequency(instance)
        schedule = intersection.compute_schedule()
        schedules.append(Schedule(intersection.id, len(schedule), schedule))

    solution = Solution(len(instance.intersections), schedules)
    solution.convert_into_file(
        "./solutions/ext_"+str(green_mean_time)+"_"+inst+".txt")
