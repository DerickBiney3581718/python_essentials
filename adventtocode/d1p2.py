from typing import List
from collections import Counter
from d1p1 import get_input

def similarity_index(location_ids_1: List[int], location_id_2: List[int])->int:
    lookup1, lookup2 = dict(Counter(location_ids_1)) , dict(Counter(location_id_2))
    return sum([ num * lookup2.get(num, 0) for num in lookup1])

l1, l2 = get_input()
print(similarity_index(l1, l2))