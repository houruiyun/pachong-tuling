#coding=utf-8
#author: 'houry'
#date: 2018/11/20
#把每一次抓到的内容保存到文件中，结尾为html
import urllib
from urllib  import request,parse
if __name__ == '__main__':
    #准备构建参数字典
    qs = {
        'kw':'张继科',
        'ie':'utf-8',
        'pn':'0'
    }
    #使用parse构建完整url
    urls = []
    baseurl = 'https://tieba.baidu.com/f?'
    for i in range(10):
        pn = i * 50
        qs['pn'] = str(pn)
        #把qs编码后和基础url进行拼接
        #拼接完成后装入url列表中
        urls.append( baseurl + parse.urlencode(qs))
    #print(urls)

    for url in urls:
        for a in range(10):
            rsp = request.urlopen(url)
            html = rsp.read().decode('utf-8')
            urllib.request.urlretrieve(url, '%s.html' %  a)
            # print(url)
            # print(html)
