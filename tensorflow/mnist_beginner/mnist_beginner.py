import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# get test data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# None means the dimension can be any length
# x is a placeholder that we will input when TensorFlow runs a computation
x = tf.placeholder(tf.float32, [None, 784])

# Variable is a modifiable tensor that lives in TensorFlow's graph of interaction operations
#   Can be used and modified by the computations
# w is weight and has shape of [784, 10] in order to multiply the 784 dimensional image vectors by it to produce 10-dimensional vectors
# b is bias has shape of [10] so we can add it to the output
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

# cross-entropy, new placeholder for correct answers
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# ask TensorFlow to minimize cross entropy using GradientDescent algorithm with a learning rate of 0.5
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# step to initialize all the variables that were created
init = tf.initialize_all_variables()

# launch model in a Session
sess = tf.Session()
sess.run(init)

# run training step 1000 times
for i in range(1000):
    # get batch of 100 random data points from training set
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# get list of booleans with actual vs expected
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# convert list of booleans into list of 1's or 0's then take the average
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

'''
    Notes: Other than running the training much more which significantly increases run time, there's not much more that
can be done in this model
'''
