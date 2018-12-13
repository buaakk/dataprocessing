# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:31:55 2018

@author: kingkong
"""

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets('./MNIST_data/',one_hot=True)

x = tf.placeholder(tf.float32,[None,784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W)+b)

y_= tf.placeholder(tf.float32,[None,10])

cross_entrop = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entrop)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    xs,ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:xs,y_:ys})
   
    
'''
评估模型
'''
c_p = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(c_p,"float"))



print(sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels}))






 