import wx
import os

def gui_kino():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Simple GUI")

    image_path = './kino.png'
    if not os.path.exists(image_path):
        print("图像文件不存在:", image_path)
        return
    
    image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
    if not image.IsOk():
        print("无法加载图像:", image_path)
        return
    
    my_pic = image.ConvertToBitmap()
    static_bitmap = wx.StaticBitmap(frame, wx.ID_ANY, my_pic)

    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    gui_kino()