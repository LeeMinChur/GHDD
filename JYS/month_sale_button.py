from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pymysql
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def month_graph():

    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    cursor = db.cursor()
    c=[]
    sql="select 주문시간,메뉴가격 from 판매내역 where month(주문시간)=month(curdate());"
    cursor.execute(sql)
    res=cursor.fetchall()

    r=[x[0] for x in res]

    r1=[x[1] for x in res]
    t=[]
    for i in r:
         t.append(i.day)

    y=[]
    sum=0



    for i in range(min(t),max(t)+1):
        sum=0
        for j in range(len(r1)):
            if t[j]==i:
                sum+=r1[j]
        y.append(sum)

    x=list(set(t))

    plt.title('{}월 매출'.format(datetime.today().month))
    plt.xticks(x)
    plt.plot(x,y,color='red',linestyle='-',marker='.', label="매출")
    plt.grid(True,linestyle='--',linewidth=0.5)

    #
    plt.xlabel('날짜')
    plt.legend(loc=2)
    plt.show()


def year_graph():

    db = pymysql.connect(host='192.168.0.7', port=3306, user='root', passwd='5284', db='Project', charset='utf8')
    cursor = db.cursor()
    c=[]
    sql="select 주문시간,메뉴가격 from 판매내역 where year(주문시간)=year(curdate());"
    cursor.execute(sql)
    res=cursor.fetchall()


    r=[x[0] for x in res]

    r1=[x[1] for x in res]
    print(r)
    print(r1)
    t=[]
    for i in r:
         t.append(i.month)

    y=[]
    sum=0



    for i in range(min(t),max(t)+1):
        sum=0
        for j in range(len(r1)):
            if t[j]==i:
                sum+=r1[j]
        y.append(sum)

    x=list(set(t))

    plt.title('{}년 매출'.format(datetime.today().year))
    plt.xticks(x)
    plt.plot(x,y,color='red',linestyle='-',marker='.', label="매출")
    plt.grid(True,linestyle='--',linewidth=0.5)

    #
    plt.xlabel('월')
    plt.legend(loc=2)
    plt.show()
