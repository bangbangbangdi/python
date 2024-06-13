# -------------------- 使用千帆AI模型 + GUI实现一个AI聊天程序 --------------------
import wx


class QianfanFrame(wx.Frame):
    def __init__(self, *arges, **kwargs):
        super().__init__(*arges, **kwargs)

    def init_ui(self):
        menubar = wx.MenuBar()
