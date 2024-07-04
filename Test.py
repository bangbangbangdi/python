import wx
import wx.richtext as rt


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 300))
        panel = wx.Panel(self)

        # 创建一个垂直方向的 BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建一个 wx.RichTextCtrl
        self.rich_text = rt.RichTextCtrl(panel, style=wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)

        # 向 wx.RichTextCtrl 中添加左对齐的文本
        self.rich_text.BeginParagraphSpacing(0, 20)
        self.rich_text.BeginAlignment(wx.TEXT_ALIGNMENT_LEFT)
        self.rich_text.WriteText("This text is left-aligned.\n")
        self.rich_text.EndAlignment()

        # 向 wx.RichTextCtrl 中添加右对齐的文本
        self.rich_text.BeginParagraphSpacing(0, 20)
        self.rich_text.BeginAlignment(wx.TEXT_ALIGNMENT_RIGHT)
        self.rich_text.WriteText("This text is right-aligned.\n")
        self.rich_text.EndAlignment()

        # 将文本框添加到垂直布局中
        vbox.Add(self.rich_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 设置面板的Sizer
        panel.SetSizer(vbox)

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "RichTextCtrl Alignment Example")
    app.MainLoop()
