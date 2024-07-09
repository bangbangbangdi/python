# -------------------- 使用千帆AI模型 + GUI实现一个AI聊天程序 --------------------
import wx
import wx.richtext as rt
import os
import qianfan


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.background_image = wx.Bitmap('../img/kuroniko.jpeg')
        self.Bind(wx.EVT_PAINT, self.on_paint)
        # 创建聊天记录框
        # self.text = wx.TextCtrl(self, size=(450, 300), style=wx.TE_READONLY)
        self.text = rt.RichTextCtrl(self, size=(450, 300), style=wx.TE_READONLY | wx.VSCROLL | wx.HSCROLL)
        self.init_text()
        self.text.SetBackgroundColour(wx.Colour(0, 0, 0, 128))
        # 创建输入文本框 并使其支持回车事件
        self.input_text = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        # 初始化文本输入框
        self.init_input_text()
        # 设定输入框的背景颜色,其中128是其透明度(macOS无效)
        self.input_text.SetBackgroundColour(wx.Colour(0, 0, 0, 128))
        # 按下回车时触发on_enter函数
        self.input_text.Bind(wx.EVT_TEXT_ENTER, self.on_enter)
        # 输入框自动获取焦点
        self.input_text.SetFocus()

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        size = self.GetSize()
        image = self.background_image.ConvertToImage()
        image = image.Scale(size.GetWidth(), size.GetHeight(), wx.IMAGE_QUALITY_HIGH)
        resized_bitmap = wx.Bitmap(image)
        dc.DrawBitmap(resized_bitmap, 0, 0, True)
        self.text.SetSize(450, size.GetHeight() - 100)

    def init_text(self):
        self.text.BeginParagraphSpacing(0, 20)
        self.text.BeginAlignment(wx.TEXT_ALIGNMENT_LEFT)
        self.text.WriteText('Hello Tin \n')
        self.text.EndAlignment()

    def init_input_text(self):
        self.input_text.SetMinSize(wx.Size(450, -1))

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddStretchSpacer()
        hbox.Add(self.text, flag=wx.ALIGN_CENTER)
        hbox.AddStretchSpacer()

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.AddStretchSpacer()
        hbox2.Add(self.input_text, flag=wx.ALIGN_CENTER)
        hbox2.AddStretchSpacer()

        vbox.Add(hbox, flag=wx.EXPAND | wx.TOP, border=20)
        # vbox.Add(self.text, proportion=1, flag=wx.EXPAND | wx.TOP, border=20)
        vbox.AddStretchSpacer()
        vbox.Add(hbox2, flag=wx.EXPAND | wx.BOTTOM, border=20)

        self.SetSizer(vbox)

    def show_answer(self, answer):
        self.text.BeginParagraphSpacing(0, 20)
        self.text.BeginAlignment(wx.TEXT_ALIGNMENT_LEFT)
        self.text.WriteText(f'{answer} \n')
        self.text.EndAlignment()

    def show_question(self, question):
        self.text.BeginParagraphSpacing(0, 20)
        self.text.BeginAlignment(wx.TEXT_ALIGNMENT_RIGHT)
        self.text.WriteText(f'{question} \n')
        self.text.EndAlignment()

    def on_enter(self, event):
        # 获取输入框内容
        text = self.input_text.GetValue()
        self.show_question(text)
        print(text)
        # 清空输入框
        self.input_text.Clear()
        res = self.chat(text)
        self.show_answer(res)

    def chat(self, question):
        os.environ["QIANFAN_AK"] = "PvSiq0beNph79ljuFcCqFPsI"
        os.environ["QIANFAN_SK"] = "ict6qgdnVdu0zs6tNJRexENlt9JCItoY"

        robot = qianfan.ChatCompletion()
        message = []
        que_dic = {"role": "user", "content": question}
        message.append(que_dic)
        resp = robot.do(
            endpoint="ernie-char-8k",
            messages=message
        )
        res = resp.body['result']
        print(res)
        message.append({"role": "assistant", "content": resp.body["result"]})
        return res


class QianfanFrame(wx.Frame):
    def __init__(self, *arges, **kwargs):
        super().__init__(*arges, **kwargs)
        self.init_ui()

    def init_ui(self):
        # 创建一个 菜单栏 对象 (因为后续的退出快捷键cmd+Q,需要它)
        menubar = wx.MenuBar()
        # 在主窗口中添加 菜单栏
        self.SetMenuBar(menubar)
        # 绑定事件 当按下cmd+Q时触发 on_quit函数
        # (这里为什么会绑定cmd+Q我也没有查到,只能暂时认为是在不指定绑定的快捷键的情况下默认就绑定的是cmd+Q吧)
        self.Bind(wx.EVT_MENU, self.on_quit)
        # 添加panel
        self.panel = MyPanel(self)

    def on_quit(self, event):
        self.Close(True)


def main():
    app = wx.App()
    ex = QianfanFrame(None, title="chat TGP", style=wx.RESIZE_BORDER | wx.CLOSE_BOX, size=(600, 500),
                      pos=(100, 100))
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
