

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=60&limit=20

# page    1  2   3   4
# start   0  20  40  60

# start （page - 1）*20


# 下载豆瓣电影前10页的数据
# （1） 请求对象的定制
# （2） 获取响应的数据
# （3） 下载数据

import urllib.parse
import urllib.request

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start':(page - 1) * 20,
        'limit':20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page,content):
    with open('douban_' + str(page) + '.json','w',encoding='utf-8')as fp:
        fp.write(content)




# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页面'))

    for page in range(start_page,end_page+1):
#         每一页都有自己的请求对象的定制
        request = create_request(page)
#         获取响应的数据
        content = get_content(request)
#         下载
        down_load(page,content)



