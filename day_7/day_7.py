from typing import List

labels_dict = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0,
               '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0,
               '2' : 0}


class Card:
    order_str = "..23456789TJQKA"

    def __init__(self, value):
        self.value = value
        self.num_value = self.order_str.rfind(value)

    def __str__(self):
        return self.value
    
    def __gt__(self, other):
        return self.num_value > other.num_value
    def __lt__(self, other):
        return self.num_value < other.num_value
    def __eq__(self, other):
        return self.value == other.value
    

class Hand:
    def __init__(self, cards: str):
        temp_cards = []
        for card in cards:
            temp_cards.append(Card(card))
        self.cards = temp_cards

    def __str__(self):
        temp_str = ""
        for item in self.cards:
            temp_str+=str(item)
        return temp_str
    


def day_7_part1(filename: str):
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    all_hands = []
    for item in data:
        cards_n_bet = item.split()
        cards = cards_n_bet[0]
        bet = cards_n_bet[1]
        temp_hand = Hand(cards)
        all_hands.append(temp_hand)
    
    for thing in all_hands:
        print(thing)


day_7_part1('day_7_test.txt')