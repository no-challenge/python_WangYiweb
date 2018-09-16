import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import html.parser
import datetime

def find(url,data1):
    global zhongshiji ,zhongshi,xiandai
    ##url="http://mc.netease.com/forum.php?mod=viewthread&tid=361277&extra=page%3D1%26filter%3Dtypeid%26typeid%3D212"
    try:
        ##url="http://mc.netease.com/forum.php?mod=viewthread&tid=363130&extra=page%3D1%26filter%3Dtypeid%26typeid%3D221"
        url_t=url
        html=urllib.request.urlopen(url_t)
        soup=BeautifulSoup(html,'lxml')
        ##soup_tag=soup.find_all("div",class_="typeoption")
        soup1_find=soup.find(class_="cgtl mbm" )
        soup_find=soup1_find.tr.next_sibling.next_sibling.next_sibling.next_sibling.find("td")
    except AttributeError:
        biaoti(url_t,data1)
    else:
        if "中世纪"in soup_find.string:
            zhongshiji=zhongshiji+1
            print(' %s  中世纪'%(data1))
        elif "中式" in soup_find.string:
            zhongshi=zhongshi+1
            print(' %s  中式'%(data1))
        elif "东亚" in soup_find.string:
            zhongshi=zhongshi+1
            print(' %s  中式'%(data1))
        elif "现代" in soup_find.string:
            xiandai=xiandai+1
            print(' %s  现代'%(data1))
        elif "特殊" in soup_find.string:
            xiandai=xiandai+1
            print(' %s  现代'%(data1))
        elif "现代/特殊" in soup_find.string:
            xiandai=xiandai+1
            print(' %s  现代'%(data1))
        else :
            None
##    


#####实现从发帖格式上找出需要的字符串 to find the information i need


def time(http1):
    global data1,soup_ezTime
    html1=urllib.request.urlopen(http1)
    soup1=BeautifulSoup(html1,'lxml')
    soup_time=soup1.find_all( 'div',attrs={'class':'authi'})
    if soup_time[1].contents[3].span==None:
        soup_relTime=soup_time[1].contents[3].string
        try:
            soup_ezTime=soup_relTime[4:13]
            data1=datetime.datetime.strptime(soup_ezTime, '%Y-%m-%d')
        except ValueError:
            soup_ezTime=soup_relTime[4:12]
            data1=datetime.datetime.strptime(soup_ezTime, '%Y-%m-%d')
    else :
        soup_reTime=soup_time[1].contents[3].span
        soup_relTime=str(soup_reTime.get('title'))
        try:
            soup_ezTime=soup_relTime[0:9]
            data1=datetime.datetime.strptime(soup_ezTime, '%Y-%m-%d')
        except ValueError:
            soup_ezTime=soup_relTime[0:8]
            data1=datetime.datetime.strptime(soup_ezTime, '%Y-%m-%d')
    return data1
######找时间  read time information


def biaoti(url,data1) :
    global zhongshiji ,zhongshi,xiandai
    ##url="http://mc.netease.com/forum.php?mod=viewthread&tid=363130&extra=page%3D1%26filter%3Dtypeid%26typeid%3D221"
    url_t=url
    html=urllib.request.urlopen(url_t)
    soup=BeautifulSoup(html,'lxml')
    soup_find=soup.find(id="thread_subject")
    if "中世纪"in soup_find.string:
        zhongshiji=zhongshiji+1
        print(' %s  中世纪'%(data1))
    elif "中式" in soup_find.string:
        zhongshi=zhongshi+1
        print(' %s  中式'%(data1))
    elif "东亚" in soup_find.string:
        zhongshi=zhongshi+1
        print(' %s  中式'%(data1))
    elif "现代" in soup_find.string:
        xiandai=xiandai+1
        print(' %s  现代'%(data1))
    elif "特殊" in soup_find.string:
        xiandai=xiandai+1
        print(' %s  现代'%(data1))
    elif "现代/特殊" in soup_find.string:
        xiandai=xiandai+1
        print(' %s  现代'%(data1))
    else :
        try:
            tupian(url)
        except AttributeError:
            print(' %s  现代'%(data1))
            xiandai=xiandai+1
    


##实现从发帖标题上找出需要的字符串 find strings from the title of post

def tupian(url):
    global soup_ezTime
    ##url="http://mc.netease.com/forum.php?mod=viewthread&tid=364044&extra=page%3D1%26filter%3Dtypeid%26typeid%3D221"
    url_t=url
    html=urllib.request.urlopen(url_t)
    soup=BeautifulSoup(html,'lxml')
    soup_png=soup.ignore_js_op.img.get('file')
    urllib.request.urlretrieve(soup_png,'c:\\Users\\57111\\Desktop\\qwq\\%s.jpg'%(soup_ezTime))


##找图片  download picture

a=1
zhongshiji=0
zhongshi=0
xiandai=0
geshi=0
while(1):
    ##url='http://mc.netease.com/forum.php?mod=forumdisplay&fid=91&filter=typeid&typeid=221&orderby=dateline'
    url='http://mc.netease.com/forum.php?mod=forumdisplay&fid=91&filter=typeid&typeid=212&orderby=dateline'
    print('需要统计的起止时间:(格式为：2018-8-13 回车 2018-8-6)')
    timeend=datetime.datetime.strptime(str(input()), '%Y-%m-%d')
    timestart=datetime.datetime.strptime(str(input()), '%Y-%m-%d')
    

    page=10           ####这里改页码  

    lol=[]  # storage url

    
    x=0
    soup_ezTime=0
    g_time=0

        
    while(a):
        for i in range(1,page):
            url_t=url+'&page='+str(i)
            html=urllib.request.urlopen(url_t)
            soup=BeautifulSoup(html,'lxml')


            for link in soup.find_all( 'a','xst'):
                data=link.get('href')
                lol.append(data)

            for whois in lol:
                http1='http:'+ whois
 ##            html1=urllib.request.urlopen(http1)
 ##            soup1=BeautifulSoup(html1,'lxml')
                data1=time(http1)
                if data1>=timestart:
                    if data1<=timeend:
                        if(data1 !=g_time):
                            print("中式：%s 中世纪：%s 现代: %s"%(zhongshi,zhongshiji,xiandai))
                            print("%s\n"%data1)
                            zhongshiji=0
                            zhongshi=0
                            xiandai=0
                        find(http1,data1)     
                        g_time=data1
                else:
                    break
                g_time=data1
            lol=[]
            a=0
        print("中式：%s 中世纪：%s 现代: %s"%(zhongshi,zhongshiji,xiandai))
    
    ##print('未通过统计 \n中式：%s\n中世纪：%s\n现代：%s\n'%(zhongshi,zhongshiji,xiandai))
    








