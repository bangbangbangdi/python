# -------------------- 补充:panel中size的作用 --------------------

# 前言:之前在02_01_simple_gui中,我们对panel的size属性的作用不是很明确
# 解答:
# 1.panel的size属性对panel中的控件布局会产生影响
# 2.如果没有显示设置panel的size大小,它会根据其所在的父容器大小来自动调整

# 以下是例子
# 观察panel的size的改变会对panel中的控件有哪些影响


import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.panel = wx.Panel(self, size=(800, 100))
        self.panel.SetBackgroundColour(wx.Colour(200, 200, 255))

        # 创建布局管理器(垂直方向) ; 这里讲一下为什么我们会需要布局管理器
        sizer = wx.BoxSizer(wx.VERTICAL)
        # 创建按钮
        button = wx.Button(self.panel, label="Click Me")
        # 将按钮添加到布局管理器中 具体参数及其解释如下
        # window: 要添加的控件。
        # proportion: 控制控件在主方向上的大小比例。默认为 0，表示不改变控件的大小；设置为大于 0 的值时，控件会按比例拉伸。
        # flag: 布局标志，可以是 wx.ALL, wx.LEFT, wx.RIGHT, wx.TOP, wx.BOTTOM, wx.EXPAND 等，用于设置边距和扩展行为。
        # border: 边距大小（像素）。
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)
        self.panel.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.change_size, button)
        self.Center()

    def change_size(self, event):
        # 此处设置的是整个Frame的大小,panel会跟着一起改变所以button按钮会始终处于垂直居中
        self.SetSize((500, 400))
        # 此处仅仅只改变panel的大小
        # self.panel.SetSize((500, 400))


def main():
    app = wx.App()
    frame = MyFrame(None, title="Panel Size Example", size=(300, 200))
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
