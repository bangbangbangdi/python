# -------------------- 线程和进程 --------------------
# 进程(Process):
# 1.是操作系统进行资源分配的最小单位
# 2.不同的进程拥有自己独立的内存空间、因此如果两个进程如果要共享数据,必须通过通信机制来实现(例如:管道、信号、套接字等)
# 线程(Thread):
# 1.是操作系统进行运算调度的最小单位
# 2.被包含在进程之中,是进程中的实际运作单位.也正是由于线程在同一进程下,因此相对于进程而言,线程间的信息共享和通信更加容易

# PS:上面只是非常简略的介绍啦...,不过目前我们有个概念就好啦~ 随着学习我们会逐渐认清它们的区别
# (稍微详细一点的我会放在ProcessOn上,当然网上还有很多更详细的长文,有兴趣可以去搜搜看~)

# -------------------- 多线程编程 --------------------
# 假设我们需要从网上下载一些文件
import random
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


# 这里参数中出现的*号,表示*号后面的参数必须使用关键字传参(额外的一些知识啦...简单了解一下就好)
def download(*, filename):
    start = time.time()
    print(f'开始下载{filename}.')
    # 这里我们让程序随机休眠一会用来模拟下载文件所需要的时间
    time.sleep(random.randint(3, 6))
    end = time.time()
    print(f'{filename}下载耗时{end - start:.3f}秒.')


# 单线程情况下
def single_thread():
    start = time.time()
    download(filename='blame')
    download(filename='奇诺之旅')
    download(filename='迷宫饭')
    end = time.time()
    print(f'总共耗时{end - start:.3f}秒.')
    # 上述的方法好慢...,而且这些下载任务并没有什么逻辑上的先后关系
    # 能不能让他们一起下载呢?


# 使用多线程情况下
def multi_thread():
    start = time.time()
    # 创建三个线程对象,并将它们放到列表中 (雇了三个工人,给他们交代好了工作内容,并准备好了工作所需的材料)
    # target : 待会要执行的函数  (交代工作内容)
    # kwargs : 关键字参数(字典)  (工作所需的材料)
    # args : 一般参数(这里没有用到)
    threads = [Thread(target=download, kwargs={'filename': 'blame'}),
               Thread(target=download, kwargs={'filename': '奇诺之旅'}),
               Thread(target=download, kwargs={'filename': '迷宫饭'})]

    # 开启线程 (让工人开始干活)
    for thread in threads:
        thread.start()

    # 等待所有线程结束 (等待所有工人完成工作)  -- 如果不好理解的话,可以把这部分注释掉再执行看看有什么区别
    for thread in threads:
        thread.join()

    end = time.time()
    print(f'总共耗时{end - start:.3f}秒.')


# 使用线程池
# 问题描述:实际上线程的创建和释放都会带来较大的开销;如何减少这种开销呢?
# 解决思路:我们可以指定一定数量的线程持续存活
#   有任务来的时候直接用(避免了线程的创建带来的开销),在任务结束的时候不销毁(避免了线程的释放的开销)
# 生活语言:
#   没有线程池:1.有工作来了 2.现场去招人(线程的创建) 3.开工(执行任务) 4.任务结束,解雇工人(线程的释放)
#   有线程池: 1.提前招好工人(维护一定的线程) 2.有工作来了 3.开工(执行任务) 4.任务结束,工人回到待命状态
def thread_pool():
    with ThreadPoolExecutor(max_workers=4) as pool:
        filenames = ['blame', '奇诺之旅', '迷宫饭']
        start = time.time()
        for file in filenames:
            pool.submit(download, filename=file)
    end = time.time()
    print(f'总耗时:{end - start:.3f}')


# 守护线程
# 问题描述:假设我们把游戏的背景音乐、分数判定、游戏的主逻辑分别交给三个线程去执行
#   当游戏主逻辑线程结束时背景音乐、分数判定当然也需要结束;即背景音乐和分数判定是和游戏主逻辑强绑定的,当主逻辑结束的时候另外两个也需要结束
#   守护线程就能完美满足上面这种需求
def display(content):
    while True:
        print(content)
        time.sleep(1)


def without_daemon_thread():
    # 此处没有设定守护线程时,就算非守护线程结束后,我们开启的线程依然会执行
    Thread(target=display, args=('ping blame',)).start()
    Thread(target=display, args=('ping kino',)).start()
    time.sleep(5)
    print('我结束啦!')


def daemon_thread():
    # 当守护线程发现只剩自己(守护线程)的时候,它就会自动结束自己的“生命” --(殉情线程..)
    Thread(target=display, args=('ping blame',), daemon=True).start()
    Thread(target=display, args=('ping kino',), daemon=True).start()
    time.sleep(5)
    print('我结束啦!')

# 资源竞争问题
# 在编写多线程代码时,不可避免的会遇到多个线程竞争同一个资源的情况.在这种情况下,如果没有合理的机制来保护被竞争的资源
# 那么就有可能出现非预期的状况.下面的代码创建了100个线程向同一个银行账户(初始余额为0元)转账,每个线程转账金额为1元
# 在正常情况下,我们的银行账户余额应该是100元,但是下面运行的代码并不能得到100元的结果

def main():
    # single_thread()
    # multi_thread()
    # thread_pool()
    # without_daemon_thread()
    daemon_thread()
    pass


if __name__ == '__main__':
    main()
