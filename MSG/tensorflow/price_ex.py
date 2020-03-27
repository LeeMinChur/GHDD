import tensorflow as tf

xData=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
yData=[55,70,90,70,50,60,70,78,10,150,250,158,300,128,170,168,189,145,150,99,98.5,15,67,89,120,150,135,180,180,350]

W=tf.Variable(tf.random_uniform([1],-10,10))
b=tf.Variable(tf.random_uniform([1],-10,10))
X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)
H=W*X+b

cost=tf.reduce_mean(tf.square(H-Y))
a=tf.Variable(0.01)

optimizer=tf.train.GradientDescentOptimizer(a)
train=optimizer.minimize(cost)
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

for i in range(5001):
    sess.run(train,feed_dict={X:xData,Y:yData})
    if i % 500 == 0:
        print(i,sess.run(cost,feed_dict={X:xData,Y:yData}),sess.run(W),sess.run(b))
for i in range(31,60):        
    print(sess.run(H,feed_dict={X:[i]}))
