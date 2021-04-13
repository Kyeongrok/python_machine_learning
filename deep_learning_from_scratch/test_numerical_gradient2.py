from tln import TwoLayerNet
import numpy as np
from dataset.mnist import load_mnist
from common.functions import *
from common.gradient import numerical_gradient


x_train, t_train, x_test, t_test = load_mnist(normalize=True, one_hot_label=True)
batch_mask = np.random.choice(x_train.shape[0], 100)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)
print(x_train)
print(x_batch.shape)
print(x_train.shape)

net = TwoLayerNet(784,100,10)

# print(net.params['W1'].shape)

loss_W = lambda W: net.loss(x_batch, t_batch)

grads = numerical_gradient(loss_W, net.params['W1'])
print(grads)

# p = np.random.rand(3, 2)
# print(p)
