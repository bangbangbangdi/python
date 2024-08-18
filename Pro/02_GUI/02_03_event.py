# -------------------- 事件03(wxPython) --------------------
import wx
import os


class EventFrame(wx.Frame):
    def __init__(self, *arges, **kwargs):
        super(EventFrame, self).__init__(*arges, **kwargs)
        self.load_saying()
        self.load_picture()
        self.init_ui()

    def init_ui(self):
        # 创建一个 菜单栏 对象
        menubar = wx.MenuBar()
        # 设置菜单栏
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_quit)
        # 创建wx.Panel组件,并指定其父容器
        self.panel = wx.Panel(self)

        # 显示图片
        self.cur_pic_index = 0
        cur_pic = self.pic_list[self.cur_pic_index]

        self.bit_map = wx.StaticBitmap(self.panel, -1, cur_pic, pos=(0, 30))
        change_btn = wx.Button(self.panel, label='Next Picture')
        carousel_btn = wx.Button(self.panel, label='Carousel', pos=(200, 4))
        stop_btn = wx.Button(self.panel, label='Stop Carousel', pos=(400, 4))
        self.Bind(wx.EVT_BUTTON, self.next_picture, change_btn)
        self.Bind(wx.EVT_BUTTON, self.carousel_start, carousel_btn)
        self.Bind(wx.EVT_BUTTON, self.carousel_stop, stop_btn)

        # 设置文本框
        self.staticText = wx.StaticText(self.panel, label=cur_pic.saying, pos=(0, 50), size=cur_pic.GetSize(),
                                        style=wx.TE_CENTRE | wx.STAY_ON_TOP)
        font = wx.Font(15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)
        # 静态文本设置成我们自己创建的字体
        self.staticText.SetFont(font)

        self.SetSize(cur_pic.GetSize())

    def load_picture(self):
        path_list = os.listdir('../img')
        path_list = ['../img/' + path for path in path_list]
        self.pic_list = []
        for path in path_list:
            bit_map = wx.Bitmap()
            bit_map.LoadFile(path)
            saying_key = path[7:].split('.')[0]
            bit_map.saying = self.saying_dic[saying_key]
            self.pic_list.append(bit_map)

    def load_saying(self):
        self.saying_dic = {}
        self.saying_dic['kino'] = '''撃つ時は、躊躇わないこと。相手が食べられる動物でも、食べられない動物でもです。
        どんな時でも、他の生き物ではなく、自分が生き残ることを最優先にしてください。……死人は、ペンを持ちません'''
        self.saying_dic['erms'] = '人間の持つポテンシャルの高さと、低さについて悩んでるとこ'
        self.saying_dic['cibo'] = 'はじめまして私はシボあなた名前は？'
        self.saying_dic['kuroniko'] = '私この身体でいられるの今日で最後なの。だから今日だけは私の思い通りに生きてみたいんだ'
        self.saying_dic['lain'] = 'そうだね、いつだって会えるよ'

    def on_quit(self, event):
        self.Close(True)

    def next_picture(self, event):
        self.cur_pic_index = 0 if self.cur_pic_index == len(self.pic_list) - 1 else self.cur_pic_index + 1
        cur_pic = self.pic_list[self.cur_pic_index]
        self.staticText.SetLabelText(cur_pic.saying)
        self.bit_map.SetBitmap(cur_pic)
        self.staticText.SetSize(cur_pic.GetSize())
        self.SetSize(self.pic_list[self.cur_pic_index].GetSize())

    def carousel_start(self, event):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.next_picture, self.timer)
        self.timer.Start(2000)

    def carousel_stop(self, event):
        self.timer.Stop()


def main():
    app = wx.App()
    ex = EventFrame(None, title="Tin's favorites", style=wx.RESIZE_BORDER | wx.CLOSE_BOX, size=(600, 600),
                    pos=(100, 100))
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
