from enum import Enum


def test(name):
    print(__name__)
    print(f"Hello {name}!")


# 牌
class Suite(Enum):
    """黑桃、红心、方块、梅花"""
    SPADE, HEART, DIAMOND, CLUB = range(4)


class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suite = '♠♥♦♣'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suite[self.suite.value]}{faces[self.face]}'


if __name__ == '__main__':
    # card = Card(suite=Suite.HEART, face=4)
    # print(card)
    # s = '你好阿'
    # print(s[0])
    # cards = []
    # for suite in Suite:
    #     for face in range(1, 14):
    #         cards.append(Card(suite=suite, face=face))
    # print(cards)

    # cards = [i for i in range(10)]
    # cards = [s.value for s in Suite]
    cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
    print(cards)

    # cards = [(suite.value, face) for suite in Suite for face in range(1, 14)]
    # cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
    # cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
    # print(cards)
