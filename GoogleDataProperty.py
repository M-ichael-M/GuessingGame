#This file property data from google dataset
import Model

def GoogleArrayAndBinary(beforeImg):
    listPx = []
    for i in range(beforeImg.shape[0]):
        value = beforeImg[i]
        if value >= 128:
            listPx.append(0)
        else:
            listPx.append(1)
    return listPx

def learn(listPx, label):
    Model.elements[-1].examples += 1
    Model.elements[-1].weights1_1 = Model.mod_wag1_1(listPx, Model.elements[-1].weights1_1, Model.elements[-1].examples)
    Model.elements[-1].weights1_2 = Model.mod_wag1_2(listPx, Model.elements[-1].weights1_2)


def LoadOne(NpList, label):
    listProcessed = GoogleArrayAndBinary(NpList)
    learn(listProcessed, label)

def Loading(labelElement, np_dataSet):
    for i in range(5):#(np_dataSet.shape[0]):
        LoadOne(np_dataSet[i, :], labelElement)




# Assuming elements is a list of objects with 'label' and 'weights1_1' and 'weights1_2' attributes
for i, element in enumerate(Model.elements):
    # Writing to the first file
    with open(f'Weights/Weights1_1/{element.label}.txt', 'w') as file:
        file.write('\n'.join(map(str, element.weights1_1)))

    # Writing to the second file
    with open(f'Weights/Weights1_2/{element.label}.txt', 'w') as file:
        file.write('\n'.join(map(str, element.weights1_2)))
