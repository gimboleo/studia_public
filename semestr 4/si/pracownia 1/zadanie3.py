'''
Rozwiązanie polega na prostym, wielokrotnym losowaniu układów kart.
Nie trzeba rozważać pełnych zasad pokera, gdyż figurant zawsze wygrywa remis (ma karty ściśle większej wartości).
'''

from random import sample



def straight_flush(hand):
    suits = hand[1]
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    for i in range(1, len(cards)):
        if cards[i] != cards[i - 1] + 1: return False
        if suits[i] != suits[i - 1]: return False
    return True


def four_of_a_kind(hand):
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    if cards[0] == cards[1] == cards[2] == cards[3] or cards[1] == cards[2] == cards[3] == cards[4]: return True
    return False


def full_house(hand):
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    if (cards[0] == cards[1] == cards[2] and cards[3] == cards[4]) or (cards[0] == cards[1] and cards[2] == cards[3] == cards[4]): return True
    return False


def flush(hand):
    suits = hand[1]

    for i in range(1, len(suits)):
        if suits[i] != suits[i - 1]: return False
    return True


def straight(hand):
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    for i in range(1, len(cards)):
        if cards[i] != cards[i - 1] + 1: return False
    return True


def three_of_a_kind(hand):
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    if cards[0] == cards[1] == cards[2] or cards[1] == cards[2] == cards[3] or cards[2] == cards[3] == cards[4]: return True
    return False


def two_pairs(hand):
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    if cards[0] == cards[1] and cards[2] == cards[3] or cards[0] == cards[1] and cards[3] == cards[4] or cards[1] == cards[2] and cards[2] == cards[3]: return True
    return False


def one_pair(hand):
    cards = [card_val[card] for card in hand[0]]
    cards.sort()

    if cards[0] == cards[1] or cards[1] == cards[2] or cards[2] == cards[3] or cards[3] == cards[4]: return True
    return False



card_val = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

figurant_deck = [
    'A1', 'A2', 'A3', 'A4',
    'K1', 'K2', 'K3', 'K4',
    'Q1', 'Q2', 'Q3', 'Q4',
    'J1', 'J2', 'J3', 'J4'
]

blotkarz_deck = [
    '21', '22', '23', '24',
    '31', '32', '33', '34',
    '41', '42', '43', '44',
    '51', '52', '53', '54',
    '61', '62', '63', '64',
    '71', '72', '73', '74',
    '81', '82', '83', '84',
    '91', '92', '93', '94',
    '101', '102', '103', '104'
]

blotkarz_cheater = ['81', '82', '83', '84', '91', '92', '93', '94', '101', '102', '103', '104']

blotkarz_cheater_2 = ['21', '31', '41', '51', '61', '71', '81', '91', '101']



def deal(n, deck):
    cards = []
    suits = []

    cards = sample(deck, n)
    suits = [int(card[-1]) for card in cards]
    cards = [card[:-1] for card in cards]

    return (cards, suits)


def play(hand_size, figurant_deck, blotkarz_deck):
    figurant_hand = deal(hand_size, figurant_deck)
    blotkarz_hand = deal(hand_size, blotkarz_deck)

    hand_ranking = [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair]

    for ranking in hand_ranking:
        fig = ranking(figurant_hand)
        blt = ranking(blotkarz_hand)

        if fig is False and blt: return (0, 1)
        if fig and blt is False: return (1, 0)
        if fig and blt: return (1, 0)



number_of_games = 10000
f_win, b_win = 0, 0
hand_size = 5

for _ in range(number_of_games):
    #result = play(hand_size, figurant_deck, blotkarz_deck)
    result = play(hand_size, figurant_deck, blotkarz_cheater)
    #result = play(hand_size, figurant_deck, blotkarz_cheater_2)
    f_win += result[0]
    b_win += result[1]

print(f'After {number_of_games} games,\n Figurant won: {f_win} games, Blotkarz: {b_win}\n')
print(f'Probability of Blotkarz winning is {b_win / number_of_games * 100}%\n')