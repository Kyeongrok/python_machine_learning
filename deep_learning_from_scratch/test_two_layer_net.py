import numpy as np
# from deep_learning_from_scratch.tln import TwoLayerNet
from deep_learning_from_scratch.two_layer_net import TwoLayerNet


net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
x = np.random.rand(100, 784)
t = net.predict(x)

grads = net.numerical_gradient(x, t)
print(grads)
