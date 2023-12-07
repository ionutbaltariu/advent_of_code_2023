strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0
}

from functools import cmp_to_key


def get_type(cards: str) -> int:
    counter = {}

    if cards == "JJJJJ":
        return 60

    for c in cards:
        # print(c)
        if c == "J":
            continue
        counter[c] = counter.get(c, 0) + 1

    max_val_card = max(counter, key=counter.get)
    cards_with_joker = cards.replace("J", max_val_card)

    counter.clear()

    for c in cards_with_joker:
        # print(c)
        counter[c] = counter.get(c, 0) + 1

    values = counter.values()
    max_val = max(values)

    if max_val in {4, 5}:
        return (max_val + 1) * 10

    # full house
    if max_val == 3:
        if all([c == 2 for c in values if c != max_val]):
            return 40

    if max_val == 3:
        if all([c == 1 for c in values if c != max_val]):
            return 30

    if max_val == 2:
        # two pair
        number_of_twos = len([c for c in values if c == 2])

        if number_of_twos == 2:
            return 20
        else:
            return 10

    # high card
    if all([c == 1 for c in values]):
        return 0

    return -1


def compare_fct(card_one, card_two):
    if card_one[1] > card_two[1]:
        return 1

    if card_one[1] < card_two[1]:
        return -1

    for card1, card2 in zip(card_one[0], card_two[0]):
        if strengths[card1] > strengths[card2]:
            return 1
        elif strengths[card1] < strengths[card2]:
            return -1

    return 0


if __name__ == "__main__":
    handler = open("7.in", "r")
    text = handler.read()
    handler.close()

    cards_container = []

    for line in text.split("\n"):
        cards, bid = line.split()
        cards_tup = (cards, get_type(cards), bid)
        cards_container.append(cards_tup)

    total_winnings = 0

    for idx, card_tup in enumerate(sorted(cards_container, key=cmp_to_key(compare_fct))):
        rank = idx + 1
        total_winnings += rank * int(card_tup[2])

    print(f"Part two, total winnings: {total_winnings}")
