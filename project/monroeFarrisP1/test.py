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


from framework import *

if __name__ == "__main__":

    """
    Testing the three main classes: 
            DataSet,
            ClassifierAlgorithm,
            Experiment
    """

    print("\nTesting the DataSet Class")
    ds = DataSet("data.csv")

    print("##########################")
    
    print("THE FILENAME IS:\n")
    print(ds.filename)

    print("\nTESTING THE CLEANING FUNCTION:")
    ds.clean()

    print("\nTESTING THE EXPLORE FUNCTION:")
    ds.explore()

    print("\n##########################")
    print("Testing the ClassifierAlgorithm Class")
    ca = ClassifierAlgorithm()

    print("\nTESTING THE TRAIN FUNCTION:")
    ca.train()

    print("\nTESTING THE TEST FUNCTION:")
    ca.test()

    print("\n##########################")
    print("Testing the Experiment Class")
    ex = Experiment()

    print("\nTESTING THE CROSS VAL FUNCTION:")
    ex.runCrossVal(5)

    print("\nTESTING THE SCORE FUNCTION:")
    ex.score()

    """
    Testing the four DataSet subclasses: 
            TimeSeriesDataSet,
            TextDataSet,
            QuantDataSet,
            QualDataSet
    """

    print("\n##########################")
    print("Testing the TimeSeriesDataSet Sub Class")
    tsds = TimeSeriesDataSet("time_series.csv")

    print("THE FILENAME IS:\n")
    print(tsds.filename)

    print("\nTESTING THE CLEANING FUNCTION:")
    tsds.clean()

    print("\nTESTING THE EXPLORE FUNCTION:")
    tsds.explore()

    print("\n##########################")
    print("Testing the TextDataSet Sub Class")
    tds = TextDataSet("text.csv")

    print("THE FILENAME IS:\n")
    print(tds.filename)

    print("\nTESTING THE CLEANING FUNCTION:")
    tds.clean()

    print("\nTESTING THE EXPLORE FUNCTION:")
    tds.explore()

    print("\n##########################")
    print("Testing the QuantDataSet Sub Class")
    qds = QuantDataSet("quant.csv")

    print("THE FILENAME IS:\n")
    print(qds.filename)

    print("\nTESTING THE CLEANING FUNCTION:")
    qds.clean()

    print("\nTESTING THE EXPLORE FUNCTION:")
    qds.explore()

    print("\n##########################")
    print("Testing the QualDataSet Sub Class")
    qualds = QualDataSet("qual.csv")

    print("THE FILENAME IS:\n")
    print(qualds.filename)

    print("\nTESTING THE CLEANING FUNCTION:")
    qualds.clean()

    print("\nTESTING THE EXPLORE FUNCTION:")
    qualds.explore()

    """
    Testing the two Experiment subclasses: 
            simpleKNNClassifier,
            kdTreeKNNClassifier
    """ 
    print("\n##########################")
    print("Testing the simpleKNNClassifier Sub Class")
    skn = simpleKNNClassifier()

    print("\nTESTING THE TRAIN FUNCTION:")
    skn.train()

    print("\nTESTING THE TEST FUNCTION:")
    skn.test()

    print("\n##########################")
    print("Testing the kdTreeKNNClassifier Sub Class")
    stn = kdTreeKNNClassifier()

    print("\nTESTING THE TRAIN FUNCTION:")
    stn.train()

    print("\nTESTING THE TEST FUNCTION:")
    stn.test()

