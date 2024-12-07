from os import path, sep, strerror
from typing import List

def get_input():
    try:
        location_ids_1 = []
        location_ids_2 = []
        inputStream =  open(f"{path.dirname(__file__)}{sep}d1p1.txt", "rt")
        line =  inputStream.readline()

        while line != '':
            id1, id2 = line.rstrip('\n').split(' ' * 3)
            location_ids_1.append(int(id1))
            location_ids_2.append(int(id2))           
            line =  inputStream.readline()
        inputStream.close()
        return location_ids_1 , location_ids_2
    except IOError as e:
        print(strerror(e.errno))
    except Exception as e:
        print(e)
        
def total_distance(location_ids_1 : List[int], location_ids_2: List[int])->int:
    location_ids_1, location_ids_2 = sorted(location_ids_1) , sorted(location_ids_2)
    return sum([ abs(val - location_ids_2[ind]) for ind,val in enumerate(location_ids_1)])

# print(get_input())
l1, l2 = get_input()
print(total_distance(l1, l2))