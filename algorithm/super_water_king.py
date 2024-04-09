# -------------------- 超级水王数 --------------------
# description:
# 给定一个只包含正整数的列表,请返回重复出现整个列表长度一半以上的数,如果没有这样的数,请返回-1
# 例如: [1,2,3,3,3,4,3,3,8] 该列表长度为 9; 其中3出现了5次 大于列表长度的一半 因此应该返回3
# [1,2,3,4,4,5,4,7,3] 该列表长度也为9;其中出现次数最多的4不过也就出现了3次,没有超过列表长度一半 因此应该返回 -1
# PS:所谓超级水王名字的由来,其实是在某个帖子里我们发现总是同一个人在发言,我们就称这个人叫水王
import random


def generate_random_list(max_length=10, max_value=3):
    # 获取随机的长度
    length = random.randint(1, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


# -------------------- 无字典版本 --------------------
# 我们尝试用现有的知识去做一下这道题
# 思路:
# 1.遍历整个列表,获取每个数都出现的多少次
#   1.1 列表中有那些不同的数字
#   1.2 这些数字各出现了多少次
# 2.看看是否有某个数真的有出现超过列表长度的一半
def use_list(ran_list):
    # 记录出现的不同的数字
    num_list = []
    # 各出现了几次
    count_list = []

    for num in ran_list:
        # 如果num没有收录在num_list的情况
        if num not in num_list:
            num_list.append(num)
            count_list.append(1)
        else:
            # 如果num已经在num_list中了,则将count_list中对应的次数+1
            idx = num_list.index(num)
            count_list[idx] += 1

    # 上述的for跑完后count_list中就已经记录好了各个数出现的次数
    half_length = len(ran_list) // 2
    index = 0
    for i in count_list:
        if i > half_length:
            return num_list[index]
        index += 1
    # 如果上述的for跑完后还没有返回,则意味着没有超级水王数
    return -1


# -------------------- 引入字典版本 --------------------
# 上面版本好麻烦啊...
# 如果有一种结构能同时存储对应的数字和出现的次数的话就好了~
# 嘿嘿~当然有啦~ 字典登场!!
# 思路:同上!
def use_dict(ran_list):
    num_dict = {}
    for num in ran_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    half_length = len(ran_list) // 2
    for key, count in num_dict.items():
        if count > half_length:
            return key
    return -1


# 怎么样~引入字典以后是是不是优雅了很多

# -------------------- 加入空间复杂度限制的版本 --------------------
# 甲方爸爸:能不能把空间压缩一下呢~ 最好能压缩到O(1)
# 这......恐怕....
# 还真可以!!

# 思路:
# 两个不同的数字对撞,如果存在超级水王数;它一定能活下来
# 但是!能活下来的不一定是超级水王数
# 因此,我们还需要拿着对撞之后活下来的数字再去遍历一次,获得具体的次数

# 具体实现:
# 变量: 候选、血量
# 规则:
# 1.如果当前血量==0,则将当前数字立为候选,血量为1
# 2.如果当前血量!=0,且当前数字==候选,血量 +1
# 3.如果当前血量!=0,且当前数字!=候选,血量 -1

def awsome_way(ran_list):
    # 候选数字
    candidate, hp = 0, 0
    # 血量
    for num in ran_list:
        if hp == 0:
            candidate, hp = num, 1
        elif num == candidate:
            hp += 1
        else:
            hp -= 1
    # 如果没有幸存者,那么绝对不存在超级水王数
    if hp == 0:
        return -1
    # 如果有幸存者,那也不能保证它就是超级水王数,我们还需要去获取它到底出现了几次
    count = 0
    for num in ran_list:
        if num == candidate:
            count += 1

    # 这里用到了三元运算符,如果暂时看不懂的话,用下面的写法是等效的
    return candidate if count > (len(ran_list) // 2) else -1

    # if count > (len(ran_list) // 2):
    #     return candidate
    # return -1


# -------------------- 由此引申出的有趣小问题 --------------------
"""
选举问题
当选条件:必须获得一半总选票以上
如果无人当选,则本次选举无效

描述:
给一定数量的选票
但是我们不能看选票的内容(到底选了谁)
唯一能操作的是一台能识别两张选票是否相同的机器
请你告诉我本次选举是否有效,以及有效情况下当选者是谁
"""


# -------------------- For Test --------------------
def test():
    test_times = 100000
    for _ in range(test_times):
        rand_list = generate_random_list()
        r1, r2, r3 = use_list(rand_list), use_dict(rand_list), awsome_way(rand_list)
        if r1 != r2 or r2 != r3 or r1 != r3:
            print(rand_list)
            print(r1, r2, r3)
            print('Oops')
            return
    print('success')


def main():
    test()


if __name__ == '__main__':
    main()
