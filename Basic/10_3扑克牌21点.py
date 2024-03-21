from enum import Enum
import random

# 21点扑克牌游戏python实现
# 游戏者的目标是使手中的牌的点数之和不超过21点且尽量大。
# 计算规则是：
# 2至9牌，按其原点数计算,A算作1点
# 10、J、Q、K牌都算作10点（一般记作T，即Ten）
""" 
21点扑克牌游戏设计思路
按下列规则模拟21点扑克牌游戏：
计算机人工智能AI作为庄家(House)，用户作为玩家(Player) 。

游戏开始时， 庄家从洗好的一副牌中发牌：第1张牌发给玩家， 第2张牌发给庄家，第3张牌发给玩家，第4张牌发给庄家。
然后，询问玩家是否需要继续“拿牌”，通过一次或多次“拿牌”，玩家尝试使手中扑克牌的点数和接近21。
如果玩家手中扑克牌的点数之和超过21，则玩家输牌。
当玩家决定 “停牌”(即，不再“拿牌”)

则轮到庄家使用下列规则(“庄家规则”)“拿牌”：
如果庄家手中的最佳点数之和小于17，则必须“拿牌”:，
如果点数之和大于或等于17，则“停牌”。
如果庄家的点数之和超过21,则玩家获胜。

最后， 比较玩家和庄家的点数。如果玩家的点数大，则获胜。如果玩家的点数小，则输牌。
如果点数相同，则平局。但玩家和庄家的牌值都是21点，此时拥有blackjack (一张Ace 和一张点数为10的牌)方获胜。
"""

# -------------------- 构建模型 --------------------

# 枚举:本质上就是符号常量,提升代码可读性,因为相比1-对应红心,HEART明显更好一些

# 花色(枚举)
class Suite(Enum):
    """黑桃、红心、方块、梅花"""
    SPADE, HEART, DIAMOND, CLUB = range(4)


"""我们可以遍历枚举,获取每一个符号常量及其对应的值"""


# for suite in Suite:
#     print(f'{suite} : {suite.value}')


# 牌
class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suite = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suite[self.suite.value]}{faces[self.face]}'


# 扑克
class Poker:

    def __init__(self):
        """实例化52张卡牌"""
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        """记录当前要发的牌的索引"""
        self.current = 0

    """洗牌"""

    def shuffle(self):
        """将索引归零"""
        self.current = 0
        """将牌随机排序"""
        random.shuffle(self.cards)

    """发牌"""

    def deal(self):
        """拿到要发的牌"""
        card = self.cards[self.current]
        self.current += 1
        return card


# poker = Poker()
# poker.shuffle()
# print(poker.cards)

# 玩家
class Player:
    def __init__(self, name):
        """玩家姓名"""
        self.name = name
        """玩家手牌"""
        self.cards = []

    def get_card(self, card):
        """拿一张牌,加入到手牌中"""
        self.cards.append(card)

    def show_card(self):
        """展示自己的手牌"""
        print(self.cards)

# -------------------- 游戏逻辑 --------------------
# 根据手牌判断得分

# 判断输赢
# def winner(p1:Player, p2:Player):
