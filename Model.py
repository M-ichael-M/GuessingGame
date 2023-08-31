#This is heart of program - AI model - it will be recognize prepare images from user
import Constants

pixels = Constants.width*Constants.height-1
class knownElements:
    def __int__(self, weights, label):
        self.weights = weights
        self.label = label
        self.examples = 1



def layer1_1(listPx, weights):
    result = 0
    layer1_1_table = []

    for i in range(pixels):
        layer1_1_table.append(listPx[i]*weights[i])
    for i in range(pixels):
        result = result + layer1_1_table[i]
    return result

def layer1_2(listPx, layer1_1, weights):
    result = 0
    layer1_2_table = []
    endResult = 0

    for i in range(pixels):
        layer1_2_table.append(listPx[i]*weights[i])
    for i in range(pixels):
        result = result + layer1_2_table[i]
    endResult = result+layer1_1
    return endResult

def layer1_3(listPx, full):
    result = (listPx/full)*100
    return result


def mod_wag1_1(new, old, examples):
    result = []
    for i in range(pixels):
        result[i] = (new[i]/examples + old[i])
    return result

def mod_wag1_2(new, old):
    result = []
    for i in range(pixels):
        if new[i] == 0:
            result[i] = old[i]-Constants.lr_1_2
    return result