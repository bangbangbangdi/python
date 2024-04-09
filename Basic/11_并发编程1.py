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
def thread_pool():

    pass


def main():
    # single_thread()
    # multi_thread()
    pass


if __name__ == '__main__':
    main()
