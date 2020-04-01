from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pymysql
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def month_graph():
    plt.figure(figsize=(15,8))
    db = pymysql.connect(host='192.168.0.13', port=3306, user='root', passwd='1234', db='Project', charset='utf8')
    cursor = db.cursor()
    c=[]

    sql="select 주문시간,메뉴가격 from 판매내역 where month(주문시간)=month(curdate());"
    cursor.execute(sql)

    res=cursor.fetchall()
    print(res)
    r=[x[0] for x in res]

    r1=[x[1] for x in res]
    t=[]
    if res==():
        x=[]
        x.append(datetime.now().day)
        y=[0]
    else:
        for i in r:
             t.append(i.day)

        y=[]
        sum = 0

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


    plt.xlabel('날짜')
    plt.legend(loc=2)
    plt.show()
    db.close()


def year_graph():
    plt.figure(figsize=(15,8))

    db = pymysql.connect(host='192.168.0.13', port=3306, user='root', passwd='1234', db='Project', charset='utf8')
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
    if res==():
        x=[]
        x.append(datetime.now().month)
        y=[0]
    else:
        print('hi')
        for i in r:
             t.append(i.month)

        y=[]
        print(min(t))
        print(max(t)+1)
        print(len(r1))
        print(len(r))
        for i in range(min(t),max(t)+1):
            sum=0
            for j in range(len(r1)):
                if t[j]==i:
                    sum+=r1[j]
            y.append(sum)

        x=list(set(t))
        print(len(y))
        if len(x) != len(y):
            for i in range(len(y)):
                if y[i]==0:
                    x.insert(i,i+1)

        print(x)
        print(y)

    plt.title('{}년 매출'.format(datetime.today().year))
    plt.xticks(x)
    plt.plot(x,y,color='red',linestyle='-',marker='.', label="매출")
    plt.grid(True,linestyle='--',linewidth=0.5)

    #
    plt.xlabel('월')
    plt.legend(loc=2)
    plt.show()
    db.close()

# month_graph()
year_graph()
