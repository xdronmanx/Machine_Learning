from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
import numpy

(X_train, y_train), (X_test, y_test) = mnist.load_data()
y_train_fix = numpy.array(
    numpy.array([([1 if j == y_train[i] else 0 for j in range(10)]) for i in range(0, len(y_train))]))
X_train = numpy.expand_dims(X_train, 1)
X_test = numpy.expand_dims(X_test, 1)
sgd = SGD(lr=0.01, momentum=0.9, decay=0.0, nesterov=True)

model = Sequential()
model.add(Dense(output_dim=64, input_dim=64, init="uniform"))
model.add(Activation("relu"))
model.add(Dense(output_dim=10, init="uniform"))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd')
model.fit(X_train, y_train_fix, batch_size=32, nb_epoch=1)
score = model.evaluate(X_test, y_test, batch_size=16)
print(score)
