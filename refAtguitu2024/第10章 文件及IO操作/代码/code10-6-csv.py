import csv,random
from my_package import my_tools
lista = []
def random_info(n=100):
    subjects = ['python','java','C++','html']
    names = []
    for i in range(n//len(subjects)):
        name = my_tools.random_string(random.randint(3, 6))
        names.append(name)
    for i in range(n):
        subject = random.choice(subjects)
        score = random.randint(50,100)
        name = random.choice(names)
        for j in lista:
            if j[0]==name and j[1]==subject:
                break
        else:
            lista.append([name,subject,score])

def average():
    with open('data.csv',mode='r',encoding='utf-8') as f:
        cf = csv.reader(f)
        head = next(cf)  #获取表头
        scores = []
        for i in cf:
            scores.append(int(i[2]))
        return sum(scores)/len(scores)


def make_datas():
    with open('data.csv',mode='a',encoding='utf-8') as f:
        cf = csv.writer(f)
        random_info()
        cf.writerows(lista)


make_datas()
# result = average()
# print('大家的平均分是',round(result,2))
