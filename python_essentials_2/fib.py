class Fib:
        def __init__(self, nn):
                self.__n = nn
                self.__i = 0
                self.__p1 = self.__p2 = 1
        def __iter__(self):
                print("__iter__")
                return self
#^ the __iter__ method is obliged to return the iterator object itself; its purpose may be a bit ambiguous here, but there's no mystery; try to imagine an object which is not an iterator (e.g., it's a collection of some entities), but one of its components is an iterator able to scan the collection; the __iter__ method should extract the iterator and entrust it with the execution of the iteration protocol; as you can see, the method starts its action by printing a message;
        
        def __next__(self):
                print("__next__")
                self.__i += 1
                if self.__i > self.__n:
                        raise StopIteration()
                
                # check first two steps
                if self.__i in (1,2):
                        return 1
                
                fibn = self.__p1 + self.__p2
                self.__p1, self.__p2 = self.__p2, fibn
                return fibn
            
for i in Fib(8):
    print(i)
    
# def adjective_to_verb(sentence, index):
#     """Change the adjective within the sentence to a verb.

#     :param sentence: str - that uses the word in sentence.
#     :param index: int - index of the word to remove and transform.
#     :return: str - word that changes the extracted adjective to a verb.

#     For example, ("It got dark as the sun set.", 2) becomes "darken".
#     """
#     sentence_list = sentence.split()
#     return f"{sentence_list[index]}en"

# input_data = ['Look at the bright sky.',
#               'His expression went dark.',
#               'The bread got hard after sitting out.',
#               'The butter got soft in the sun.',
#               'Her eyes were light blue.',
#               'The morning fog made everything damp with mist.',
#               'He cut the fence pickets short by mistake.',
#               'Charles made weak crying noises.',
#               'The black oil got on the white dog.']
# index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]

# for index, test in enumerate(input_data):
#     print(test, adjective_to_verb(test, index_data[index]), sep=" : ")
    

# def is_pangram(sentence):
#     if len(sentence) < 26:
#         return False
#     alph = "abcdefghijklmnopqrstuvwxyz"
#     alph_dict = {}
#     for char in alph:
#         alph_dict[char] = 0

#     for char in sentence.lower():
#         if char.isalpha():
#             alph_dict[char] = 1
#     print(alph_dict.values(), len(alph_dict.values()))     
#     return sum(list(alph_dict.values())) >= 26

# is_pangram("abcdefghijklmnopqrstuvwxyz")