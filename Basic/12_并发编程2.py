# -------------------- 多进程编程 --------------------
# 问题描述:对于官方的python解释器而言,我们无法通过多线程的方式将CPU的使用率突破100%,
#   但是对于现在多核计算机而言CPU使用率100%仅仅意味着将一个CPU跑满,其他CPU都在摸鱼(一人干活,多人围观)
#   为了更加充分的使用CPU的计算能力,我们可以使用多进程
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import current_process, Process, Queue
from time import sleep


# -------------------- 单进程和多进程的区别 --------------------
def to_travel(character, locations):
    """
    输出谁去哪里旅行
    :param character: 旅人
    :param locations: 旅行的地点列表
    :return:
    """
    # current_process()能获取当前进程对象
    print(f'PID:{current_process().pid}')
    print(f'Name:{current_process().name}')
    sleep(1)
    while len(locations) != 0:
        print(f'{character} travels to the {locations[0]}')
        locations.pop(0)
        sleep(0.4)


def single_process():
    """单进程的执行to_travel函数"""
    lis = ['クロニコのながぐつ', '人の痛みがわかる国', '多数決の国', '大人の国', '東亜重工']
    to_travel('kaiba', lis)
    to_travel('kino', lis)
    to_travel('kiri', lis)


def multi_process():
    """多进程的执行to_travel函数"""
    lis = ['クロニコのながぐつ', '人の痛みがわかる国', '多数決の国', '大人の国', '東亜重工']
    Process(target=to_travel, args=('kaiba', lis)).start()
    Process(target=to_travel, args=('kino', lis)).start()
    to_travel('kiri', lis)


"""对比上述单进程和多进程的执行结果,可以更好的感受到他们之间的区别"""

# -------------------- 多进程和多线程的区别 --------------------
PRIMES = [
             1116281,
             1297337,
             104395303,
             472882027,
             533000389,
             817504243,
             982451653,
             112272535095293,
             112582705942171,
             112272535095293,
             115280095190773,
             115797848077099,
             1099726899285419
         ] * 5


def is_prime(num):
    """判断素数(了解一下就好了,涉及到一些数论...原理我也搞不太清楚...;重点在于通过这个栗子,体会多进程和多线程的区别)"""
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def multi_thread_prime():
    """多线程版本(注意我们用的是ThreadPool-线程池)"""
    with ThreadPoolExecutor(max_workers=16) as executor:
        """下面这种写法可能会有点陌生,可以参照下面的补充解释"""
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')


def multi_process_prime():
    """多进程版本(注意我们用的是ProcessPool-进程池)"""
    with ProcessPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'number: {number} is prime: {prime}')


# -------------------- 进程间通信 --------------------
# 哈喽啊~
# 看了一下上次正式更新的时间,居然已经过了10天了...
# 闲言少叙,我们接着撸代码!
# 在讲 "进程间通信"之前我们先尝试做这样一件看似简单的事情:
#   启动两个进程,一个进程输出“Tin” 一个进程输出“Bang”,当两个进程输出的“Tin”和“Bang”加起来一共有50个时,就结束程序;
counter = 0


def without_communication_task(content):
    global counter
    while counter < 50:
        print(content, counter, flush=True)
        counter += 1
        sleep(0.1)


# 我们先来看看没有进程通信的情况下是什么样子的
def without_communication():
    Process(target=without_communication_task, args=('Tin',)).start()
    Process(target=without_communication_task, args=('Bang',)).start()


'''
通过观察我们发现,Tin和Bang居然各打印了50次
其实原因也不难理解,因为每个进程都有自己独立的内存空间,这也就意味着有两个完全不搭嘎的counter存在于他们各自的进程中
并在各自的进程中都从0加到50,因此Tin和Bang都各自打印了50次

进程A和进程B的情况可以类比为两个人在各自的小黑屋里执行自己的任务
A看不到B,B也看不到A
而我们的任务是需要他们协同完成的,即A和B都能读取且修改同一个变量counter(进程间的通信)
'''


def communication_task(content, queue):
    count = queue.get()
    while count < 50:
        print(content, count)
        count += 1
        queue.put(count)
        sleep(0.1)
        count = queue.get()


def process_communication():
    queue = Queue()
    queue.put(0)
    p1 = Process(target=communication_task, args=('Tin', queue))
    p1.start()
    p2 = Process(target=communication_task, args=('Bang', queue))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    """
    这里还需要往队列里添加50的原因在于:
    当调用queue.get()时,如果queue内没有数据,进程会处于阻塞的状态(进程不会终止)
    而我们在循环内只会往queue中放入一次50,拿到50的进程会跳出循环条件(进程终止)
    剩下的另一个进程则要面对一个空的queue(进程阻塞)
    因此我们需要手动往queue中再次放入50让另一个进程也终止
    (天呐...这个解释起来害蛮麻烦的;到时候我画个图吧)
    """
    queue.put(50)


def main():
    # single_process()
    # multi_process()
    """使用time python 12_并发编程2.py 执行;
    观察最后的输出结果中cpu使用率,对比多线程和多进程
    (是不是有点晕~hhh,放轻松,目前有个概念就好啦~) """

    """通过观察可以发现,多线程情况下cpu使用率只能逼近100%,没有榨干多核cpu的性能"""
    # multi_thread_prime()

    """通过观察可以发现,多进程情况下cpu使用率能简单的突破100%(具体多少与CPU核心数相关,m1是660%),相比多线程能更好榨干cpu性能"""
    # multi_process_prime()

    """进程通信测试"""
    # without_communication()
    process_communication()

    # queue = Queue()
    # queue.put(10)
    # print(queue.get())
    # # queue.put(20)
    # print(queue.get())

    pass


if __name__ == '__main__':
    main()
