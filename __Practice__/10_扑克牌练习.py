from enum import Enum
import random

# 花色(枚举)
class Suite(Enum):
    # 黑桃，红桃，方块，梅花
    SPADE, HEART, DIAMOND, CLUB = range(4) 


# for suite in Suite:
    # print(f'{suite} : {suite.value}')

class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    
    def __repr__(self):
        suite = '♠♥♣♦'
        face = ['', 'A', '2','3','4','5','6','7','8','9','10','J','Q','K']
        return f'{suite[self.suite.value]}{face[self.face]}'
    
if __name__ == '__main__':
    card = Card(suite=Suite.HEART, face=9)
    print(card)