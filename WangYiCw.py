import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import html.parser 



while(1):
    url='http://mc.netease.com/forum.php?mod=forumdisplay&fid=91&filter=typeid&typeid=221&orderby=dateline'
    print('页数为')
    page=int(input())+1


    lol=[]
    zhongshiji=0
    zhongshi=0
    xiandai=0
    geshi=0
    www=0
    a='昨天'
        

    for i in range(1,page):
        url_t=url+'&page='+str(i)
        html=urllib.request.urlopen(url_t)
        soup=BeautifulSoup(html,'lxml')


        for link in soup.find_all( 'a','xst'):
            data=link.get('href')
            lol.append(data)

        for whois in lol:
            http1='http:'+ whois
            html1=urllib.request.urlopen(http1)
            soup1=BeautifulSoup(html1,'lxml')
            soup1_find=soup1.find(text=['中式','东亚','中世纪','现代','特殊','现代/特殊'])
            soup_time=soup1.find_all( 'div',attrs={'class':'authi'})
            try:
                soup_reTime=str(soup_time[1].contents[3].span.string)

            except AttributeError:
                break
            else:
                print(soup_reTime)
                soup_ezTime=soup_reTime[:3]
                
                if soup_ezTime <'8天前':
                    if soup1_find == '中式':
                        zhongshi=zhongshi+1
                    elif soup1_find=='中世纪':
                        zhongshiji=zhongshiji+1
                    elif soup1_find=='现代':
                        xiandai=xiandai+1
                    elif soup1_find=='东亚':
                        zhongshi=zhongshi+1
                    elif soup1_find=='特殊':
                        xiandai=xiandai+1
                    elif soup1_find=='现代/特殊':
                        xiandai=xiandai+1
                    else:
                        geshi=geshi+1

                elif '昨天' in soup_reTime:
                    if soup1_find == '中式':
                        zhongshi=zhongshi+1
                    elif soup1_find=='中世纪':
                        zhongshiji=zhongshiji+1
                    elif soup1_find=='现代':
                        xiandai=xiandai+1
                    elif soup1_find=='特殊':
                        xiandai=xiandai+1
                    elif soup1_find=='东亚':
                        zhongshi=zhongshi+1
                    else:
                        geshi=geshi+1
                elif '前天' in soup_reTime:
                    if soup1_find == '中式':
                        zhongshi=zhongshi+1
                    elif soup1_find=='中世纪':
                        zhongshiji=zhongshiji+1
                    elif soup1_find=='现代':
                        xiandai=xiandai+1
                    elif soup1_find=='特殊':
                        xiandai=xiandai+1
                    elif soup1_find=='东亚':
                        zhongshi=zhongshi+1
                    else:
                        geshi=geshi+1
            
        lol=[]
                
              
              
        
              
           
    print('未通过统计')
    print("中式: " )
    print(zhongshi)
    print("中世纪: " )
    print(zhongshiji)
    print("现代: " )
    print(xiandai)
    print("格式: " )
    print(geshi)



    ###通过
    
    url='http://mc.netease.com/forum.php?mod=forumdisplay&fid=91&filter=author&orderby=dateline&typeid=212'
    print('页数为')
    page=int(input())+1


    lol=[]
    zhongshiji=0
    zhongshi=0
    xiandai=0
    geshi=0
    www=0
    a='昨天'
        

    for i in range(1,page):
        url_t=url+'&page='+str(i)
        html=urllib.request.urlopen(url_t)
        soup=BeautifulSoup(html,'lxml')


        for link in soup.find_all( 'a','xst'):
            data=link.get('href')
            lol.append(data)

        for whois in lol:
            http1='http:'+ whois
            html1=urllib.request.urlopen(http1)
            soup1=BeautifulSoup(html1,'lxml')
            soup1_find=soup1.find(text=['中式','东亚','中世纪','现代','特殊','现代/特殊'])
            soup_time=soup1.find_all( 'div',attrs={'class':'authi'})
            try:
                soup_reTime=str(soup_time[1].contents[3].span.string)

            except AttributeError:
                break
            else:
                print(soup_reTime)
                soup_ezTime=soup_reTime[:3]
                
                if soup_ezTime <'8天前':
                    if soup1_find == '中式':
                        zhongshi=zhongshi+1
                    elif soup1_find=='中世纪':
                        zhongshiji=zhongshiji+1
                    elif soup1_find=='现代':
                        xiandai=xiandai+1
                    elif soup1_find=='东亚':
                        zhongshi=zhongshi+1
                    elif soup1_find=='特殊':
                        xiandai=xiandai+1
                    elif soup1_find=='现代/特殊':
                        xiandai=xiandai+1
                    else:
                        geshi=geshi+1

                elif '昨天' in soup_reTime:
                    if soup1_find == '中式':
                        zhongshi=zhongshi+1
                    elif soup1_find=='中世纪':
                        zhongshiji=zhongshiji+1
                    elif soup1_find=='现代':
                        xiandai=xiandai+1
                    elif soup1_find=='特殊':
                        xiandai=xiandai+1
                    elif soup1_find=='东亚':
                        zhongshi=zhongshi+1
                    else:
                        geshi=geshi+1
                elif '前天' in soup_reTime:
                    if soup1_find == '中式':
                        zhongshi=zhongshi+1
                    elif soup1_find=='中世纪':
                        zhongshiji=zhongshiji+1
                    elif soup1_find=='现代':
                        xiandai=xiandai+1
                    elif soup1_find=='特殊':
                        xiandai=xiandai+1
                    elif soup1_find=='东亚':
                        zhongshi=zhongshi+1
                    else:
                        geshi=geshi+1
            
        lol=[]
                
              
              
        
              
           
    print('通过统计')
    print("中式: " )
    print(zhongshi)
    print("中世纪: " )
    print(zhongshiji)
    print("现代: " )
    print(xiandai)
    print("格式: " )
    print(geshi)










    

