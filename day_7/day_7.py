from collections import Counter


class Card:
    order_str = ".J23456789T@QKA"

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
        return self.num_value == other.num_value


class Hand:
    def __init__(self, cards: str):
        temp_cards = []
        for card in cards:
            temp_cards.append(Card(card))
        self.cards = temp_cards
        self.hand_value = self.setHand_value(cards)

    def setHand_value(self, cards: str):
        card_count = Counter(cards)
        sorted_card_count = sorted(card_count.items(),
                                   key=lambda x: x[1], reverse=True)
        if (sorted_card_count[0][1] == 5):
            return 7
        if (sorted_card_count[0][1] == 4):
            return 6
        if (sorted_card_count[0][1] == 3):
            if sorted_card_count[1][1] == 2:
                return 5
            return 4
        if (sorted_card_count[0][1] == 2):
            if sorted_card_count[1][1] == 2:
                return 3
            return 2
        return 1

    def __str__(self):
        temp_str = ""
        for item in self.cards:
            temp_str += str(item)
        return temp_str

    def __eq__(self, other):
        x = zip(self.cards, other.cards)
        for pair in x:
            if (pair[0] != pair[1]):
                return False
        return True

    def __lt__(self, other):
        if (self.hand_value == other.hand_value):
            x = zip(self.cards, other.cards)
            for pair in x:
                if (pair[0] != pair[1]):
                    return pair[0] < pair[1]
            return False
        else:
            return self.hand_value < other.hand_value

    def __gt__(self, other):
        if (self.hand_value == other.hand_value):
            x = zip(self.cards, other.cards)
            for pair in x:
                if (pair[0] != pair[1]):
                    return pair[0] > pair[1]
            return False
        else:
            return self.hand_value > other.hand_value


class Hand2:
    def __init__(self, cards: str):
        temp_cards = []
        for card in cards:
            temp_cards.append(Card(card))
        self.cards = temp_cards
        self.hand_value = self.setHand_value(cards) 

    def setHand_value(self, cards: str):
        joker_count = cards.count('J')
        no_jokers = cards.replace('J', '')
        card_count = Counter(no_jokers)
        sorted_card_count = sorted(card_count.items(),
                                   key=lambda x: x[1], reverse=True)
        if (joker_count == 5):
            return 5.0
        if (sorted_card_count[0][1] == 5):
            return 5.0
        if (sorted_card_count[0][1] == 4):
            return 4.0 + joker_count
        if (sorted_card_count[0][1] == 3):
            if len(sorted_card_count) > 1:
                if sorted_card_count[1][1] == 2:
                    return 3.5
                else:
                    return 3.0 + joker_count
            else:
                return 3.0 + joker_count
        if (sorted_card_count[0][1] == 2):
            if len(sorted_card_count) > 1:
                if sorted_card_count[1][1] == 2:
                    return 2.5 + joker_count
                else:
                    return 2.0 + joker_count
            else:
                return 2.0 + joker_count
        return 1.0 + joker_count

    def __str__(self):
        temp_str = ""
        for item in self.cards:
            temp_str += str(item)
        return temp_str

    def __eq__(self, other):
        x = zip(self.cards, other.cards)
        for pair in x:
            if (pair[0] != pair[1]):
                return False
        return True

    def __lt__(self, other):
        if (self.hand_value == other.hand_value):
            x = zip(self.cards, other.cards)
            for pair in x:
                if (pair[0] != pair[1]):
                    return pair[0] < pair[1]
            return False
        else:
            return self.hand_value < other.hand_value

    def __gt__(self, other):
        if (self.hand_value == other.hand_value):
            x = zip(self.cards, other.cards)
            for pair in x:
                if (pair[0] != pair[1]):
                    return pair[0] > pair[1]
            return False
        else:
            return self.hand_value > other.hand_value


def day_7_part1(filename: str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    all_hands = []
    for item in data:
        cards_n_bet = item.split()
        cards = cards_n_bet[0]
        bet = cards_n_bet[1]
        temp_hand = Hand(cards)
        all_hands.append((temp_hand, bet))
    sorted_hands = sorted(all_hands)
    total_winnings = 0
    for i, h in enumerate(sorted_hands):
        total_winnings += (i+1)*int(h[1])

    return total_winnings


def day_7_part2(filename: str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    all_hands = []
    for item in data:
        cards_n_bet = item.split()
        cards = cards_n_bet[0]
        bet = cards_n_bet[1]
        temp_hand = Hand2(cards)
        all_hands.append((temp_hand, bet))
    sorted_hands = sorted(all_hands)
    total_winnings = 0
    for i, h in enumerate(sorted_hands):
        print(h[0], h[0].hand_value,  h[1])
        total_winnings += (i+1)*int(h[1])

    return total_winnings


def handTesting():
    a = "AAAAA"
    b = "AAA8A"
    c = "23456"
    handA = Hand(a)
    handB = Hand(b)
    handC = Hand(c)
    hands = [handA, handB, handC]
    hands_sorted = sorted(hands)
    for thing in hands_sorted:
        print(str(thing))


print(day_7_part2("day_7_input.txt"))
