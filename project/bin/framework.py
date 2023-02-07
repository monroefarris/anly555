class DataSet:

    def __init__(self, filename):
        self.filename = filename

    def __readFromCSV(self, filename):
        print("reading the CSV file")

    def __load(self, filename):
        print("loading the data")

    def clean(self):
        print("cleaning the data")

    def explore(self):
        print("exploring the data")

class TimeSeriesDataSet(DataSet):
    pass

class TextDataSet(DataSet):
    pass

class QuantDataSet(DataSet):
    pass

class QualDataSet(DataSet):
    pass 


class ClassifierAlgorithm:

    def __init__(self):
        pass

    def train(self):
        print("training algorithm")

    def test(self):
        print("testing algorithm")

class simpleKNNClassifier(ClassifierAlgorithm):
    pass

class kdTreeKNNClassifier(ClassifierAlgorithm):
    pass


class Experiment:

    def runCrossVal(self, k):
        print("cross validation with k = " + str(k))

    def score(self):
        print("score function")

    def __confusionMatrix(self):
        print("confusion matrix function")

