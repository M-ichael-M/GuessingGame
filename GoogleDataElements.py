import GoogleDataProperty as GP
import Model
import Constants
import numpy as np

def LoadElements():
    labelElement = "EiffelTower"
    np_dataSet = np.load('GoogleDataSet/EiffelTower.npy')
    Model.elements.append(Model.knownElements(Constants.weightsAll0, Constants.weightsAll0, labelElement))
    GP.Loading(labelElement, np_dataSet)

    labelElement = "AircraftCarierr"
    np_dataSet = np.load('GoogleDataSet/AircraftCarierr.npy')
    Model.elements.append(Model.knownElements(Constants.weightsAll0, Constants.weightsAll0, labelElement))
    GP.Loading(labelElement, np_dataSet)

    labelElement = "Airplane"
    np_dataSet = np.load('GoogleDataSet/Airplane.npy')
    Model.elements.append(Model.knownElements(Constants.weightsAll0, Constants.weightsAll0, labelElement))
    GP.Loading(labelElement, np_dataSet)

    labelElement = "GreatWallChina"
    np_dataSet = np.load('GoogleDataSet/GreatWallChina.npy')
    Model.elements.append(Model.knownElements(Constants.weightsAll0, Constants.weightsAll0, labelElement))
    GP.Loading(labelElement, np_dataSet)

    labelElement = "MonaLisa"
    np_dataSet = np.load('GoogleDataSet/MonaLisa.npy')
    Model.elements.append(Model.knownElements(Constants.weightsAll0, Constants.weightsAll0, labelElement))
    GP.Loading(labelElement, np_dataSet)
