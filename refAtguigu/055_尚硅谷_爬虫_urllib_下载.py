import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# url代表的是下载的路径  filename文件的名字
# 在python中 可以变量的名字  也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
# url_img = 'https://img1.baidu.com/it/u=3004965690,4089234593&fm=26&fmt=auto&gp=0.jpg'
#
# urllib.request.urlretrieve(url= url_img,filename='lisa.jpg')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-mhkku4ndaka5etk3/1080p/cae_h264/1629557146541497769/mda-mhkku4ndaka5etk3.mp4?v_from_s=hkapp-haokan-tucheng&auth_key=1629687514-0-0-7ed57ed7d1168bb1f06d18a4ea214300&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest='

urllib.request.urlretrieve(url_video,'hxekyyds.mp4')