import numpy as np
import matplotlib.pyplot as plt
import random
from Block import Block

MIN_PROD = 10
MAX_PROD = 100
KURTOSIS_FACTOR = 0.8
DAYS = 1
STEP = 10 #minutes
MINUTES_IN_DAY = 1440
INCREMENT_PROB = 0.05
NUMBER_OF_BLOCKS = 2000
BASE_SPACE_RATIO = 0.25



def generateCurve():
    currentProduction = MIN_PROD
    basic_prob = 0
    samples = int((MINUTES_IN_DAY * DAYS) / STEP)
    curve = [0] * samples
    for i in range(0, samples):
        if (i <= int(samples / 2)):
            curve[i] = currentProduction
        else:
            curve[samples - (i - int(samples/2))] = currentProduction
        increment = 0
        # if (i < int(samples / 2)):
        increment = (MAX_PROD- currentProduction) * basic_prob if (basic_prob > random.uniform(0, 1)) else 0
        currentProduction += int(increment)
        # else:
        #     increment = (MAX_PROD - currentProduction) * basic_prob if (basic_prob > random.uniform(0, 1)) else 0
        #     currentProduction += int(increment)
        if (increment == 0):
            basic_prob += INCREMENT_PROB
        else:
            basic_prob = 0
        if (i == int(samples/2)):
            currentProduction = MIN_PROD
    return curve

def generateBlocks():
    max_base = int(((MINUTES_IN_DAY * DAYS) / STEP) * BASE_SPACE_RATIO)
    blocks = []
    for i in range(0, NUMBER_OF_BLOCKS):
        base = int(random.uniform(1, max_base))
        height = int(random.uniform(1, MAX_PROD))
        deadline = int(random.uniform(1, int((MINUTES_IN_DAY * DAYS)/ STEP)))
        blocks.append(Block(i, base, height, deadline))
    return blocks




inputFile = open("input-generated.txt", "w")
curve = generateCurve()
plt.step(np.array(range(0, len(curve))), np.array(curve), 'r', where='post')
plt.show()
inputFile.write(' '.join(map(str, curve)) + "\n")
blocks = generateBlocks()
for b in blocks:
    inputFile.write(str(b.base) + " " + str(b.height) + " " + str(b.deadline) + "\n")
inputFile.close()

    

