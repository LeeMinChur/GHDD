import tensorflow as tf
xData=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
yData=[2000000,2500000,1500000,1700000,1800000,1300000,990000,780000,1000000,1105800,1560000,4000000,5000000,3000000,1900000,780000,1900000,1600000,450000,980000,886500,853200,1500000,780000,458000,680000,2250000,3000000,1235400,500000]

W=tf.Variable(tf.random_uniform([1],-100,100))
b=tf.Variable(tf.random_uniform([1],-100,100))

X=tf.placeholder(tf.float32,name="X")
Y=tf.placeholder(tf.float32,name="Y")

H=W*X+b


cost=tf.reduce_mean(tf.square(H-Y))

optmizer=tf.train.GradientDescentOptimizer(learning_rate=0.00001)
train_op=optmizer.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(8001):
        sess.run(train_op,feed_dict={X:xData,Y:yData})
        if step%1==0:
            print(step,sess.run(cost,feed_dict={X:xData,Y:yData}),sess.run(W),sess.run(b))
    print("\n==================Test================")
    for i in range(31,61):
        print("X:",i-30," Y:",sess.run(H,feed_dict={X:i}))
   #print("X:32, Y:",sess.run(H,feed_dict={X:32}))
