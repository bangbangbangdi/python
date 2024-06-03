import random


def test(name: str):
    print('Tin')
    print(name)
    print(type(name))


def test2() -> list:
    res = '10'
    return [] if random.randint(1, 2) > 1 else 'zzz'
    # return res


def main():
    # test('123')
    res = test2()
    print(res)
    print(type(res))
    # print(res)

    pass


if __name__ == '__main__':
    main()
