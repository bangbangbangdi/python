# 2024-05-18 临时学习笔记(刚刚写年份的时候恍惚了一下...已经2024年了嘛...)
class Card():
    def __init__(self, face):
        self.face = face

    def __repr__(self):
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # return f'face: {self.face}'
        return f'face: {faces[self.face]}'

def main(num):
    faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    print(faces[num])

    card = Card(13)
    print(card)
    print(card.face)

if __name__ == '__main__':
    main(12)
    main(1)
