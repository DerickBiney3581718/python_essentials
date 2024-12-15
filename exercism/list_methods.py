def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    return queue.index(friend_name)
test_data = [
((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye'), ['RobotGuy', 'WW', 'HawkEye']),
((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 1, 'RichieRich'), ['Tony', 'Bruce', 'RichieRich']),
((['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 1, 'Okoye'), ['Agatha', 'Pepper', 'Valkyrie', 'Okoye']),
((['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 0, 'Gamora'), ['Drax', 'Nebula', 'Gamora']),
]

for each in test_data:
    print(add_me_to_the_queue(*each[0]))
    print('answer:', each[1])