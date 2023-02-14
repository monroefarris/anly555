#* framework.py                            
#*                                                 
#*  ANLY 555 Spring 2023                     
#*  Project Monroe 
#*                                                 
#*  Due on: 2/12/2023                  
#*  Author(s): Monroe Farris                           
#*  
#* 
#*  In accordance with the class policies and Georgetown's 
#*  Honor Code, I certify that, with the exception of the  
#*  class resources and those items noted below, I have neither 
#*  given nor received any assistance on this project other than  
#*  the TAs, professor, textbook and teammates.  
#* 

class DataSet:
    """
    Class that defines the characteristics of a data set to later 
    be used for analysis. 
    """

    def __init__(self, filename):
        """
        filename: name of data file to be processed 
        """

        self.filename = filename

    def __readFromCSV(self, filename):
        """
        Function to read in data from a CSV file 

        filename: name of data file to be processed 
        """

        print("reading the CSV file")

    def __load(self, filename):
        """
        Function to load data for analysis 

        filename: name of data file to be processed 
        """

        print("loading the data")

    def clean(self):
        """
        Function for cleaning the data.
        """

        print("cleaning the data")

    def explore(self):
        """
        Function for exploring the data.
        """

        print("exploring the data")

class TimeSeriesDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    time series data 
    """

    pass

class TextDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    text data 
    """

    pass

class QuantDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    quantitative data 
    """
    pass

class QualDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    qualitative data 
    """

    pass 


class ClassifierAlgorithm:
    """
    Class that defines the characteristics of a 
    classifier algorithm to perform analysis on 
    the data 
    """

    def __init__(self):
        pass

    def train(self):
        """
        Function for training data.
        """

        print("training algorithm")

    def test(self):
        """
        Function for testing data 
        """

        print("testing algorithm")

class simpleKNNClassifier(ClassifierAlgorithm):
    """
    Class inherited from the ClassifierAlgorithm class that 
    will be used to define the characteristics of 
    a simple KNN Classifier 
    """

    pass

class kdTreeKNNClassifier(ClassifierAlgorithm):
    """
    Class inherited from the ClassifierAlgorithm class that 
    will be used to define the characteristics of 
    a simple KD Tree KNN Classifier 
    """

    pass


class Experiment:
    """
    Class that defines the characteristics of an 
    experimentation approach to perform analysis on 
    the data 
    """

    def runCrossVal(self, k):
        """
        Function to perform cross validation 

        k: number of groups the data will be split into
        """

        print("cross validation with k = " + str(k))

    def score(self):
        """
        Function that calculates a score for the data 
        based on evaluation metrics 
        """

        print("score function")

    def __confusionMatrix(self):
        """
        Function that generates a confusion matrix 
        for the analysis 
        """

        print("confusion matrix function")

