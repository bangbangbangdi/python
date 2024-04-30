import random,re,time
a = []
n = 5
def random_char(upper=True):
    if upper:
        t = random.randint(ord('A'),ord('Z'))
        return chr(t)
    else:
        t = random.randint(ord('a'),ord('z'))
        return chr(t)
def random_string(length):
    s = ''
    for i in range(length):
        s += random_char(random.choice([True,False]))
    return s

def yan_zheng_ma(length):
    return random_string(length)

def is_phone_number(phone):
    # 手机号码
    result = re.match(r'^1\d{10}$', phone)
    if result==None:
        return '非法手机号！'
    return '正确的手机号'

def is_id_number(ids):
    result = re.match(r'^\d{6}((20[012][01234])|(1[89]\d\d))\d{7}([\dX])$', ids)
    if result == None:
        return '非法身份证号！'
    return '正确的身份证号'


def get_time():
    t = time.localtime()
    s = time.strftime('%Y-%m-%d %H:%M:%S', t)
    return s

def main():
    # a = []
    # for i in range(20):
    #     a.append(random_string(random.randint(3,6)))
    # print(a)
    print(yan_zheng_ma(8))