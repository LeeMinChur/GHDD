import pymysql
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from new8.sql_and_query import pysql
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


def graph_pri():
    plt.figure(figsize=(15,8))
    db = pymysql.connect(host='192.168.0.13', port=3306, user='root', passwd='1234', db='Project', charset='utf8')
    cursor = db.cursor()


    sql="select 주문시간,메뉴가격 from 판매내역 where month(주문시간)=month(curdate());"
    cursor.execute(sql)
    res=cursor.fetchall()

    r=[x[0] for x in res]
    r1=[x[1] for x in res]
    t=[]

    for i in r:
         t.append(i.day)
    x=list(set(t))
    print("x :" , x)
    y=[]
    sum=0

    for i in range(min(t),max(t)+1):
        sum=0
        for j in range(len(r1)):
            if t[j]==i:
                sum+=r1[j]
        y.append(sum)
    #--------------------------------------------------------------------------------------------------#
    xData=x
    print("x : ",x)
    yData=y
    print("y : ", y)

    W=tf.Variable(tf.random_uniform([1],-1.0,1.0))
    b=tf.Variable(tf.random_uniform([1],-1.0,1.0))
    X=tf.placeholder(tf.float32,name="X")
    Y=tf.placeholder(tf.float32,name="Y")
    H=W*X+b

    cost=tf.reduce_mean(tf.square(H-Y))
    optmizer=tf.train.GradientDescentOptimizer(learning_rate=0.0001)
    train_op=optmizer.minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for step in range(6000):
            sess.run(train_op,feed_dict={X:xData,Y:yData})
            if step%200==0:
                print(step,sess.run(cost,feed_dict={X:xData,Y:yData}),sess.run(W),sess.run(b))
        print("\n==================예측결과================")
        x = []
        y = []
        for i in range(31,61):
            # print("X:",i-30," Y:",sess.run(H,feed_dict={X:i}))
            x.append(i - 30)
            y.append(int(sess.run(H,feed_dict={X:i})))

        for i in range(0,30):
            print("다음 달 매출 예측: ", x[i]," 일  ", y[i], " 원 ")

    plt.title('다음달 매출 예측')
    plt.xticks(x)
    plt.plot(x,y,color='r',marker='.',linestyle='-', label="value")
    plt.grid(True,linestyle='--',linewidth
    =0.5)
    #
    plt.xlabel('day')
    # plt.ylael('매출')
    plt.legend(loc=2)
    db.close()
    plt.show()

graph_pri()

