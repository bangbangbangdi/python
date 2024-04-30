import turtle,time
from  my_package import my_tools
pen = turtle.Turtle()
pen.backward(100)
pen.speed(0)
while True:
    time.sleep(1)
    times = my_tools.get_time()
    pen.clear()
    pen.write(times,font=("Arial",40,"normal"))
input()