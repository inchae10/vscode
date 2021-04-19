'''
python vs tensorflow diff
'''

x = 10
y = 20
z = x + y
print("z=", z)

# import tensorflow as tf # ver 2.0
import tensorflow.compat.v1 as tf # ver 1.0
tf.disable_v2_behavior()  # ver2.x 사용 안함

print(tf.__version__)

x = tf.constant(10)  # 상수 정의  <tf.Tensor 'Const_2:0' shape=() dtype=int32>
y = tf.constant(20)  # 상수 정의  <tf.Tensor 'Const_3:0' shape=() dtype=int32>

z = x + y
print("z =" , z) # <tf.Tensor 'add_2:0' shape=() dtype=int32>

sess = tf.Session()  # 상수, 변수, 식 ->  device(CPU, GPU, TPU)에 할당
#sess.list_devices()


print("x=", sess.run(x)) # x = 10
print("y=", sess.run(y)) # x = 20

# sess.run(x,y) error

x_val, y_val = sess.run([x,y])
print(x_val, y_val) # 10 20

print("z=", sess.run(z)) # x, y 상수 참조 -> 연산 z= 30

sess.close()











