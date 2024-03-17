import random
import math

w = []

savedPattern = []

amountOfUserPattern = len(savedPattern)

userPattern = input("Input the binary pattern you want to save(Enter 2 to end): ").split(",")
while userPattern != ['2']:
    print(userPattern)
    savedPattern.append([])
    for i in range(len(userPattern)):
        savedPattern[amountOfUserPattern].append(int(userPattern[i]))
    amountOfUserPattern += 1
    userPattern = input("Input the binary pattern you want to save(Enter 2 to end): ").split(",")

lr = 0.001

training = True

def perceptron(input_, expected, w, lr):
    global training
    output = 0
    for i in range(len(input_)):
        output += input_[i] * w[i]
    output = round(output)
    error = output - expected
    for i in range(len(input_)):
        w[i] -= error * lr
    return error

times = 0
errorList = []
totalError = 0

while training:
    if w == []:
        for n in range(len(savedPattern)):
            w.append([])
            for i in range(len(savedPattern[n])):
                w[n].append(random.random())
    for n in range(len(savedPattern)):
        error = perceptron(savedPattern[n], n+1, w[n], lr)
        errorList.append(error)
    for i in range(len(errorList)):
        totalError += math.sqrt(errorList[i] ** 2)
    if totalError == 0:
        training = False
    errorList = []
    totalError = 0
    times += 1
    if times >= 10000:
        w = []
        times = 0

input_ = input("Input the binary pattern(Enter 2 to end): ").split(",")

while input_ != ['2']:
    output = 0
    for i in range(len(input_)):
        input_[i] = int(input_[i])
    #print(input_)
    if input_ in savedPattern:
        for i in range(len(w[savedPattern.index(input_)])):
            output += input_[i] * w[savedPattern.index(input_)][i]
        output_ = round(output)
        print("It is pattern number", output_, "in memory.")
    else:
        print("Pattern does not exist in memory.")
    input_ = input("Input the binary pattern(Enter 2 to end): ").split(",")
