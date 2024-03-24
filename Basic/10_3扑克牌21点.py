from enum import Enum
import random

# 21点扑克牌游戏python实现
# 游戏者的目标是使手中的牌的点数之和不超过21点且尽量大。
# 计算规则是：
# 2至9牌，按其原点数计算,A算作1点或者11点(例如 A(1) + J(10) = 21 ; A(1) + 9 + J(10) = 20)
# 10、J、Q、K牌都算作10点（一般记作T，即Ten）
""" 
21点扑克牌游戏设计思路
按下列规则模拟21点扑克牌游戏：
计算机人工智能AI作为庄家(House)，用户作为玩家(Player) 。

游戏开始时， 庄家从洗好的一副牌中发牌：
玩家、庄家各抓两张牌
然后，询问玩家是否需要继续“拿牌”，通过一次或多次“拿牌”，玩家尝试使手中扑克牌的点数和接近21。
如果玩家手中扑克牌的点数之和超过21，则玩家输牌。
当玩家决定 “停牌”(即，不再“拿牌”)

则轮到庄家使用下列规则(“庄家规则”)“拿牌”：
如果庄家手中的最佳点数之和小于17，则必须“拿牌”:，
如果点数之和大于或等于17，则“停牌”。
如果庄家的点数之和超过21,则玩家获胜。

最后， 比较玩家和庄家的点数。如果玩家的点数大，则获胜。如果玩家的点数小，则输牌。
如果点数相同，则平局。但玩家和庄家的牌值都是21点，此时拥有blackjack (一张Ace 和一张点数为10的牌)方获胜,双方都是blackJack则平局。
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
        self.shuffle()

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

    def get_card(self, poker, size):
        """拿size张牌,加入到手牌中,并返回最后一张牌"""
        card = None
        for _ in range(size):
            card = poker.deal()
            self.cards.append(card)
        return card

    def show_card(self):
        """展示自己的手牌"""
        print(f'{self.name}手牌为:{self.cards}')


# -------------------- 游戏逻辑 --------------------
def is_blackjack(cards: list[Card]) -> bool:
    """
    判断是否是一张A和一张10或J,Q,K
    :param cards: 手牌列表
    :return:是否是blackJack
    """
    if len(cards) != 2:
        return False
    if cards[0].face != 1 and cards[1].face != 1:
        return False
    if cards[0].face == 1 and not (cards[1].face in range(10, 14)):
        return False
    if cards[1].face == 1 and not (cards[0].face in range(10, 14)):
        return False
    return True


# print(is_blackjack([Card(Suite.SPADE, 1), Card(Suite.SPADE, 13)]))
# print(is_blackjack([Card(Suite.SPADE, 1), Card(Suite.SPADE, 10)]))
# print(is_blackjack([Card(Suite.SPADE, 2), Card(Suite.SPADE, 10)]))
# print(is_blackjack([Card(Suite.SPADE, 1), Card(Suite.SPADE, 10), Card(Suite.SPADE, 10)]))


def get_count(cards: list[Card]) -> int:
    """
    根据手牌判断得分
    :param cards: 手牌列表
    :return: 手牌对应的得分
    """
    if is_blackjack(cards):
        return 21
    count = 0
    for card in cards:
        count += card.face
    return count


# cs = [Card(Suite.HEART, 10), Card(Suite.SPADE, 11)]
# print(get_count(cs))

def winner(p1: Player, p2: Player):
    """
    判断输赢 - 这个有个潜台词,即能来到这一步的双方手牌分数均不超过21点
    :param p1: 玩家1
    :param p2: 玩家2
    :return: 获胜的玩家 0-None; 1-玩家1获胜; 2-玩家2获胜
    """
    cards1 = p1.cards
    cards2 = p2.cards

    p1.show_card()
    p2.show_card()
    """我们先来纠结一下是否有人是blackjack的情况"""
    if is_blackjack(cards1) and is_blackjack(cards2):
        print('两位神仙都是blackjack,这把平局')
    elif is_blackjack(cards1):
        print(f'{p1.name}获胜')
    elif is_blackjack(cards2):
        print(f'{p2.name}获胜')

    """都不是blackjack的情况下"""
    if get_count(cards1) == get_count(cards2):
        print(f'{p1.name}分数为:{get_count(p1.cards)} ; {p2.name}分数为:{get_count(p2.cards)}.平局')
    elif get_count(cards1) > get_count(cards2):
        print(f'{p1.name}分数为:{get_count(p1.cards)} ; {p2.name}分数为:{get_count(p2.cards)}.{p1.name}获胜')
    else:
        print(f'{p1.name}分数为:{get_count(p1.cards)} ; {p2.name}分数为:{get_count(p2.cards)}.{p2.name}获胜')


def game_init(poker: Poker) -> list[Player]:
    """
    游戏初始化
    :return: 返回玩家列表,其中第一个元素为玩家,第二个元素为庄家
    """
    print("欢迎来到21点！")
    name = input("怎么称呼?") or 'bang'
    player = Player(name)
    banker = Player("庄家")
    player.get_card(poker, 2)
    banker.get_card(poker, 2)
    player.show_card()
    banker.show_card()
    return [player, banker]


def player_loop(poker: Poker, player: Player) -> bool:
    """
    玩家抓牌循环
    :param poker:
    :param player:
    :return:
    """
    while True:
        count = get_count(player.cards)
        """这里后面的 or 是逻辑运算符的另一个种用法,以后会讲到"""
        answer = input(f'{player.name},您当前的分数为{count},要继续抓牌嘛?y/n') or 'y'
        if answer.lower() == 'y':
            """抓一张牌"""
            card = player.get_card(poker, 1)
            print(f'您抓到的牌是{card}')
            player.show_card()
            count = get_count(player.cards)
            if count > 21:
                print(f'抱歉...您当前分数为{count} 爆了,庄家获胜')
                return True
        else:
            return False


def bank_loop(poker: Poker, banker: Player) -> bool:
    """
    庄家抓牌循环
    :param poker:
    :param banker:
    :return:
    """
    while True:
        """庄家抓牌逻辑为 < 17 就抓"""
        count = get_count(banker.cards)
        print(f'庄家当前分数为{count}')
        if count < 17:
            card = banker.get_card(poker, 1)
            print(f'庄家抓到的牌是{card}')
            banker.show_card()
            count = get_count(banker.cards)
            if count > 21:
                print(f'庄家分数为{count} 爆了,玩家获胜')
                return True
        else:
            return False


def main():
    """
    游戏主循环
    :return:
    """
    """游戏初始化"""
    poker = Poker()
    player, banker = game_init(poker)
    """玩家抓牌 返回值是True则意味着玩家抓爆了"""
    if player_loop(poker, player):
        return
    """庄家抓牌 返回值是True则意味着庄家抓爆了"""
    if bank_loop(poker, banker):
        return
    """判断获胜"""
    winner(player, banker)


if __name__ == '__main__':
    main()

# -------------------- Practice --------------------
# 自己将整个游戏再重写一遍,并将当前游戏改成三局两胜制
