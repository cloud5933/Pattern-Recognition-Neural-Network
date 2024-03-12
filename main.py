import random
import math

w = []
w2 = []
w3 = []
w4 = []

circle = [
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0
]
triangle = [
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
    1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0
]
cross = [
    1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0,
    1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1
]
heart = [
    0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0
]

one = [0, 0, 0, 1, 1, 1, 0, 0,
       0, 0, 1, 1, 1, 1, 0, 0,
       0, 1, 1, 0, 1, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 0, 0]

two = [0, 0, 1, 1, 1, 1, 0, 0,
       0, 1, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 0, 0, 0, 1, 0,
       0, 0, 0, 0, 0, 1, 1, 0,
       0, 0, 0, 0, 1, 1, 0, 0,
       0, 0, 0, 1, 1, 0, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 0,
       0, 1, 1, 1, 1, 1, 1, 0]

three = [0, 0, 1, 1, 1, 1, 0, 0,
         0, 1, 0, 0, 0, 0, 1, 0,
         0, 0, 0, 0, 0, 0, 1, 0,
         0, 0, 1, 1, 1, 1, 1, 0,
         0, 0, 0, 0, 0, 0, 1, 0,
         0, 0, 0, 0, 0, 0, 1, 0,
         0, 1, 0, 0, 0, 0, 1, 0,
         0, 0, 1, 1, 1, 1, 0, 0]

four = [0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 1, 0]

lr = 0.001

training = True

def preceptron(input_, expected, w, lr):
    global training
    if w == []:
        for i in range(len(input_)):
            w.append(random.random())
    output = 0
    for i in range(len(input_)):
        output += input_[i] * w[i]
    output = round(output)
    error = output - expected
    for i in range(len(input_)):
        w[i] -= error * lr
    print("output:", output, "error:", error)
    return error

times = 0

while training:
    if (preceptron(one, 1, w, lr) == preceptron(two, 2, w, lr) == preceptron(three, 3, w2, lr) ==
    preceptron(four, 4, w2, lr) == preceptron(circle, 5, w3, lr) == preceptron(triangle, 6, w3, lr) ==
    preceptron(heart, 7, w4, lr) == 0):
        training = False
    times += 1
    if times >= 10000:
        w = []
        w2 = []
        w3 = []
        w4 = []
        times = 0

while 1:
    output = 0
    input_ = input("Input the binary form of the shape: ").split(", ")
    for i in range(len(input_)):
        input_[i] = int(input_[i])
    print(input_)
    if input_ == one or input_ == two:
        for i in range(len(w)):
            output += input_[i] * w[i]
    if input_ == three or input_ == four:
        for i in range(len(w2)):
            output += input_[i] * w2[i]
    if input_ == circle or input_ == triangle:
        for i in range(len(w3)):
            output += input_[i] * w3[i]
    if input_ == heart:
        for i in range(len(w4)):
            output += input_[i] * w4[i]
    output = round(output)
    print(output)
