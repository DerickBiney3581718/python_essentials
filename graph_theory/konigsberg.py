from typing import List
from itertools import chain
# seven bridges abcdefg
# four land areas ABCD
#? Can a path be created

BRIDGES = [
    'AaB', 'AbB', 'AcC', 'AdC', 'AeD', 'CgD', 'DfB'
]

# list of paths for each starting point

# output : ['AbBcDeFgD']
def get_walks_from_starting_area(area:str, bridges:List[str]=BRIDGES)->List[str]:
    walks = []
    
    def make_a_walk(area:str, bridges:List[str], crossed:str=[], path:str='' ):
        path = path or area
        # find available bridges from the area
        uncrossed_bridges = [bridge for bridge in bridges if bridge not in crossed and area in bridge]
        if not uncrossed_bridges:
            walks.append(path)
            
        for bridge in uncrossed_bridges:
            path += bridge[1:] if bridge[0] == area else bridge[1::-1]
            make_a_walk(path[-1], bridges, [bridge, *crossed],path)
    
    make_a_walk(area, bridges)
    
    return walks
def main():
    chain_obj = chain.from_iterable([get_walks_from_starting_area(area) for area in 'ABCD'])
    print(len([path for path in chain_obj if len(path) ==  14]))
    
if __name__ == '__main__':
    main()