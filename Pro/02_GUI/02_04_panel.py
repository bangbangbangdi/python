# -------------------- 补充:panel中size的作用 --------------------

# 前言:之前在02_01_simple_gui中,我们对panel的size属性的作用不是很明确
# 解答:panel的size属性对panel中的控件布局会产生影响
# 以下是例子

import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        # super(MyFrame, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)

        self.panel = wx.Panel(self, size=(800, 100))
        self.panel.SetBackgroundColour(wx.Colour(200, 200, 255))

        sizer = wx.BoxSizer(wx.VERTICAL)
        button = wx.Button(self.panel, label="Click Me")
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)
        self.panel.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.change_size, button)
        self.Center()

    def change_size(self, event):
        self.SetSize((500, 400))
        # self.panel.SetSize((500, 400))


def main():
    app = wx.App()
    frame = MyFrame(None, title="Panel Size Example", size=(300, 200))
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
