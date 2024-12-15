"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_of_card = 5
    if card in 'JQK':
        value_of_card = 10
    elif card == 'A':
        value_of_card = 1
    else:
        value_of_card = int(card)
    return value_of_card
    



def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_val, card_two_val = value_of_card(card_one), value_of_card(card_two)
    if card_one_val == card_two_val : 
        return card_one, card_two
    return card_one if card_one_val > card_two_val else card_two
            


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    return 11 if (value_of_card(card_one) + value_of_card(card_two)) <= 10 else 1
test_data = [('2', '3', 11), ('3', '6', 11), ('5', '2', 11),
             ('8', '2', 11), ('5', '5', 11), ('Q', 'A', 1),
             ('10', '2', 1), ('7', '8', 1), ('J', '9', 1),
             ('K', 'K', 1), ('2', 'A', 1), ('A', '2', 1)]


for (card_one, card_two, ace_value) in test_data:
    if value_of_ace(card_one, card_two) != ace_value:
        print(card_one, card_two, ace_value, value_of_ace(card_one, card_two))
